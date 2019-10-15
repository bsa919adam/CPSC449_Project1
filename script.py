import json
import requests
import resp as resp
import tracks as tracks

trackdata ={
    'title':'title'
    'artist':'artist'
    'length':'length'
    'link':'track_url'
}

newtrack={
    'title': 'title'
    'artist': 'artist'
    'album': 'album'
    'length': 'length'
    'description': 'description'
}

playlistdata={
    'playlist_url':'playlist_url'
    'title': 'title'
    'artist': 'artist'
    'album': 'album'
    'length': 'length'
    'description': 'description'
}
userdata={
    'username': 'username'
    'displayname':'displayname'
}

newplaylistdata{
'playlist_url':'playlist_url'
}

tracks = requests.get('/api/v1/tracks', trackdata,json = tracks)
if tracks.status_code != 200:
    raise ApiError('GET /tracks {}'.format(tracks.status_code))
    print(tracks,trackdata.json)

new = requests.post('/api/v1/tracks/new', newtrack, json = new)
if tracks.status_code != 200:
    raise ApiError('GET /tracks {}'.format(new.status_code))
    print(new,newtrack.json)

playlist = request.get('/api/v1/playlists/all',playlistdata,json = playlist)
if playlist.status_code != 200:
    raise ApiError('GET /all {}'.format(rest.status_code))
    print(playlist,playlistdata)

user = requests.get('/api/v1/playlists/<user>', userdata,json = user)
if user.status_code != 200:
    raise ApiError('GET /user {}'.format(user.status_code))
    print(user,userdata.json)

newplaylist = request.post('/api/v1/playlists/new',newplaylistdata, json = newplaylist)
if newplaylist.status_code != 200:
    raise ApiError('POST /new {}'.format(newplaylist.status_code))
    print(newplaylist,newplaylistdata.json)