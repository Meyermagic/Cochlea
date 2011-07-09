#!/usr/bin/env python2
import threading, Queue, socket, MySQLdb, mutagen, json, subprocess, os.path, os

def copytags(src, dst):
    source = mutagen.File(src, easy=True)
    dest = mutagen.File(dst, easy=True)
    for key in source:
        try:
            dest[key] = source[key]
        except:
            pass
    dest.save()

def convert(src, dst):
    working_dir = os.path.dirname(os.path.realpath(__file__))
    p1 = subprocess.Popen(['ffmpeg', '-i', src, '-v', '0', '-f', 'wav', '-'], cwd=working_dir, stdin=open('/dev/null', 'r'), stdout=subprocess.PIPE, stderr=open('/dev/null', 'w'))
    p2 = subprocess.Popen(['lame', '--pad-id3v2-size', '1024', '-S', '-V', '9', '--resample', '44.1', '-', dst], cwd=working_dir, stdin=p1.stdout, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
    p1.stdout.close()
    p2.wait()

class Convertor(threading.Thread):
    def __init__(self, conversionQueue):
        self.cq = conversionQueue
        threading.Thread.__init__(self)
    def run(self):
        while True:
            task = self.cq.get()
            
            if task is not None:
                #Process the task
                conn, addr = task
                
                #Grab the data and close the connection
                data = json.loads(conn.recv(1024))
                conn.send("accepted")
                conn.close()
                
                #Actually start the conversion process
                sourcefile = './uploads/' + data['id']
                destfile = './audio/' + data['id'] + '.mp3'
                
                print "Starting", data['id']
                
                #Create mp3 copy
                convert(sourcefile, destfile)
                
                #Copy over the tags
                copytags(sourcefile, destfile)
                
                #Remove the original
                os.remove(sourcefile)
                
                print "Finished", data['id']
                
                #Update the song in the database
                pass

def startServer(port, concurrentThreads=1):
    try:
        #No limit to conversion in queue
        conversionQueue = Queue.Queue(0)
        threadPool = []
        
        #Populate the thread pool
        for i in range(concurrentThreads):
            threadPool.append(Convertor(conversionQueue))
        
        #Start all the threads
        for thread in threadPool:
            thread.start()
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #We only want local connections
        server.bind(('127.0.0.1', port))
        server.listen(5)
        
        while True:
            conversionQueue.put(server.accept())
    except:
        for thread in threadPool:
            thread.join()
        server.close()


if __name__ == "__main__":
    startServer(40234, 2)