import json
import requests
import resp as resp
import tracks as tracks

newtrack={
    'title': 'title',
    'artist': 'artist',
    'album': 'album',
    'length': 'length',
    'description': 'description',
}

newplaylistdata={
'playlist_url':'playlist_url',
}

tracks = requests.get('/api/v1/tracks',newtrack,json = tracks)
if tracks.status_code != 200:
    raise ApiError('GET /tracks {}'.format(tracks.status_code))
    print(tracks,newtrack=newtrack.json)

new = requests.post('/api/v1/tracks/new', json = new)
if tracks.status_code != 200:
    raise ApiError('GET /tracks {}'.format(new.status_code))
    print(new)

playlist = request.get('/api/v1/playlists/all',json = playlist)
if playlist.status_code != 200:
    raise ApiError('GET /all {}'.format(rest.status_code))
    print(playlist)

user = requests.get('/api/v1/playlists/<user>',json = user)
if user.status_code != 200:
    raise ApiError('GET /user {}'.format(user.status_code))
    print(user)

newplaylist = request.post('/api/v1/playlists/new',newplaylistdata, json = newplaylist)
if newplaylist.status_code != 200:
    raise ApiError('POST /new {}'.format(newplaylist.status_code))
    print(newplaylist,newplaylistdata = newplaylistdata.json)