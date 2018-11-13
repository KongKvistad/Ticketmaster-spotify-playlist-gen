import spotipy
import spotipy.util as util

# spoofy credentials here
from config2 import CLIENT_ID, CLIENT_SECRET, CLIENT_REDIRECT_URI

import random
import requests
import ticketpy
import sys

tm_client = ticketpy.ApiClient('TM credentials here')
events = tm_client.events.find(
	#parameters TM api

	#city="Oslo",
	#segment_id='KZFzniwnSyZfZ7v7nJ',
	#classificationId= 'KZFzniwnSyZfZ7v7nJ',
	#start_date_time='2018-06-30T00:00:00Z',
	#end_date_time='2018-07-02T00:00:00Z',
)

mylist = []

for i in events:
	for event in i:
		mylist.append(event.name) 


mylist_sorted = []

for ele in mylist:
    if ele not in mylist_sorted:
        mylist_sorted.append(ele)

print(mylist_sorted)

scope = 'playlist-modify-private'
username = 'eirikpews'
playlist_name = 'ticketmaster test!'
playlist_desc = "testy test"

token = util.prompt_for_user_token(username,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=CLIENT_REDIRECT_URI)
spotify = spotipy.Spotify(auth=token)



artist_uris_cut = []

ls = []

for x in mylist_sorted:

	results = spotify.search(q='artist:' + x, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		artist = items[0]
		artist_uris_cut.append(artist['uri'])



		for y in artist_uris_cut:
			top_tracks = spotify.artist_top_tracks(y)['tracks']
		for track in top_tracks[:1]:
		    ls.append(track['uri'])


playlist_create = spotify.user_playlist_create(username, playlist_name, public = False)
playlist_id = str(playlist_create['id'])
track_ids = ls  
add_tracks = spotify.user_playlist_add_tracks(username, playlist_id, track_ids)

print(ls)
