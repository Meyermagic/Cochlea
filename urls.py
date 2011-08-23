from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Figure out which of these works
    (r'^$', 'cochlea.views.index'),
    (r'^/$', 'cochlea.views.index'),
    
    #Channels
    (r'^(?P<channel_name>\w+)/$', 'cochlea.views.channel'),
    
    #AJAX Views, all JSON responses
    
    #Sync info (current song ID and position in song)
    (r'^(?P<channel_name>\w+)/sync/$', 'cochlea.views.channel_sync'),
    
    #Playlist info (all songs in playlist, votes for each song)
    (r'^(?P<channel_name>\w+)/playlist/$', 'cochlea.views.channel_playlist'),
    
    #Song votes (map of song ID to # of votes)
    (r'^(?P<channel_name>\w+)/votes/$', 'cochlea.views.channel_votes'),
    
    #Users (list of users in channel)
    (r'^(?P<channel_name>\w+)/users/$', 'cochlea.views.channel_users'),
    
    #Chat log (messages in channel, after specific time)
    (r'^(?P<channel_name>\w+)/log/$', 'cochlea.views.channel_log'),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
