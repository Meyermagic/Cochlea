import threading, Queue, subprocess, socket, json, mutagen, os, os.path, argparse
from django.core.management.base import NoArgsCommand
from django.conf import settings
from cochlea.models import Song
MEDIA_ROOT = settings.MEDIA_ROOT

def copy_tags(src, dst):
    source = mutagen.File(src, easy=True)
    dest = mutagen.File(dst, easy=True)
    for key in source:
        try:
            dest[key] = source[key]
        except:
            pass
    dest.save()
    #I'm pretty sure all the fields are lists so that the tags can have multiple values.
    #If that isn't the case, then we'll be grabbing the first character of the tag strings.
    #TODO: Check this.
    return (dest.info.length, dest.get('title', [''])[0], dest.get('artist', [''])[0], dest.get('album', [''])[0])

def real_convert(src, dst):
    #TODO: Check source file's integrity/readability by ffmpeg first, and return errors if we need to.
    #KNOWN BUGS: The ffmpeg decoding step fails on http://integerzero.net/music/2-19%20_Libera%20me_%20from%20hell.mp3
    p1 = subprocess.Popen(['ffmpeg', '-i', src, '-v', '0', '-f', 'wav', '-'], stdin=open('/dev/null', 'r'), stdout=subprocess.PIPE, stderr=open('/dev/null', 'w'))
    p2 = subprocess.Popen(['lame', '--pad-id3v2-size', '1024', '-S', '-V', '9', '--resample', '44.1', '-', dst], stdin=p1.stdout, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
    p1.stdout.close()
    p2.wait()
    #Current error test is simply checking to see if the destination file exists
    return os.path.isfile(dst)

class Convertor(threading.Thread):
    def __init__(self, conversionQueue):
        self.queue = conversionQueue
        #Is there a reason to use threading.Event() here instead?
        self.stopped = False
        threading.Thread.__init__(self)
    def run(self):
        while not self.stopped:
            try:
                data = self.queue.get(True, 1.0)
            except Queue.Empty:
                continue
            #Determine source and destination files
            src = os.path.join(MEDIA_ROOT, 'uploads/'+data['id'])
            dst = os.path.join(MEDIA_ROOT, 'audio/'+data['id']+'.mp3')
            
            #Process the task
            print "Converting", data['id']
            status = real_convert(src, dst)
            print "Done converting", data['id']
            
            if not status:
                pass
                #If we errored out, set the song to an error state
                #TODO: This
                #s = Song.objects.get(pk=data['id'])
            else:
                #If we didn't error out:
                #Copy over tags
                metadata = copy_tags(src, dst)
                
                #TODO: Update status and metadata on corresponding song entry
                #s = Song.objects.get(pk=data['id'])
            
            #Remove original file
            os.remove(src)
            
            #Tell everyone we finished a task
            self.queue.task_done()
    def stop(self):
        self.stopped = True

def convert(song_spec, port=40234):
    #All we need is the song's unique ID
    data = json.dumps({'id' : song_spec})
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', port))
    client.send(data)
    client.close()

#if __name__ == "__main__":
def main():
    #Nice CLI options
#    parser = argparse.ArgumentParser(description='Handle asynchonous audio file conversion.')
#    parser.add_argument('--workers', '-w', dest='workers', default=1, type=int, help='maximum number of concurrent conversions', metavar='N')
#    parser.add_argument('--port', '-p', dest='port', default=40234, type=int, help='the port for the conversion server to listen on', metavar='PORT')
#    
#    args = parser.parse_args()
    
    concurrent_workers = 2#args.workers
    port = 40234#args.port
    queue = Queue.Queue(0)
    threadPool = []
    
    #Populate the thread pool with workers
    for i in range(concurrent_workers):
        threadPool.append(Convertor(queue))
    
    #Start the workers
    for thread in threadPool:
        thread.start()
    
    #Build server to listen for conversion tasks on
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #We only want local connections
    server.bind(('127.0.0.1', port))
    server.listen(5)
    
    try:
        #Put connections into the queue
        while True:
            #Grab the data and close the connection
            conn, addr = server.accept()
            data = json.loads(conn.recv(1024))
            queue.put(data)
            conn.send("accepted")
            conn.close()
    except:
        pass
    finally:
        #Close server
        server.close()
        
        #Wait for the queue to empty
        queue.join()
        
        #Tell threads to exit
        for thread in threadPool:
            thread.stop()
        
        #Wait for threads to exit
        for thread in threadPool:
            thread.join()

#TODO: This, correctly.
class Command(NoArgsCommand):
    help = "Whatever you want to print here"

    def handle_noargs(self, **options):
        main()
