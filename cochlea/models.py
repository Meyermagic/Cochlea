from django.db import models
from random import getrandbits

def rand(bits):
    return hex(getrandbits(bits))[2:].rstrip('L')

class Channel(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=20)
    channel = models.ForeignKey(Channel)

class Song(models.Model):
    uploader = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)
    STATUS_CHOICES = (
        (0, 'Uploading'),
        (1, 'Converting'),
        (2, 'Ready'), 
        (3, 'Error')
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    votes = models.IntegerField()
    ident = models.CharField(max_length=32, primary_key=True)
    audio = models.FileField(upload_to='audio')
    #Metadata fields
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.FloatField()
    #Give us a probably unique ID. Might use more secure RNG later.
    #Or can we just rely on the auto-incrementing primary key Django will do for us?
    def save(self, *args, **kwargs):
        self.ident = rand(128)
        super(Song, self).save(*args, **kwargs)

class Message(models.Model):
    sender = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)
    #content
    #time
