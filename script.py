import code
import json
import requests
from flask_api import request

newtrack={
    "title": "Rush",
    "artist": "Ryan Oakes",
    "length": "5:13",
    'link': "http://www.tuneboost.net/track/TnEAmdOLa",
    'artwork': 'https://art/cool/pic',
}
newtrack = {
    "title": "Such A Simple Thing",
    "artist": "Ray LaMontagne",
    "length": "4:56",
    "link": "https://mp3.pm/song/107844868/Ray_LaMontagne_-_Such_A_Simple_Thing/",
    "artwork":"https://genius.com/Ray-lamontagne-such-a-simple-thing-lyrics",
}

newtrack = {
    "title": "Godspeed You",
    "artist": "Francesco Rossi feat. Ozark Henry",
    "length": "318",
    "link": "https://mp3.pm/artist/5570/7_Svezhaki_Radio_Record/",
    "artwork":"https://imagescdn.junodownload.com/full/CS2491383-02A-BIG.jpg",
}


newplaylistdata={
    "title": "Jazz",
    "creator":"John",
    "description":"A collection of Jazz music",
    "tracks":{
        "track1":"https://mp3.pm/artist/115845/Mississippi_John_Hurt/",
        "track2":"https://mp3.pm/song/1939223/Mississippi_John_Hurt_-_Candy_Man/",
        "track3":"https://mp3.pm/song/76320417/Mississippi_John_Hurt_-_Trouble_I_Had_All_My_Days/",
        "track4":"https://mp3.pm/song/76351794/Mississippi_John_Hurt_-_Got_the_Blues_Can_t_Be_Satisfied/",
    }
}
newplaylistdata={
    "title": "Acoustic & Vocals",
    "creator":"Craig",
    "description":"Mix of acoustic music with vocals diff. artist",
    "tracks":{
        "track1":"https://mp3.pm/song/128087879/Coldplay_-_Yellow/",
        "track2":"https://mp3.pm/song/128087880/Merlin_Menson_-_Coma_White_Acoustic/",
        "track3":"https://mp3.pm/song/1556/Ed_Sheeran_-_You_Need_Me_I_Dont_Need_You/",
        "track4":"https://mp3.pm/song/7400079/Bon_Jovi_-_Its_My_Life_acoustic/",
        "track5":"https://mp3.pm/song/128087896/Boyce_Avenue_feat.Fifth_Harmony_Kevin_Smith_-_Mirrors_Justin_Timberlake_Cover/",
    }
}

newplaylistdata={
    "title": "Etnic",
    "creator":"Craig",
    "description":"Music from the world, sounds and vocals",
    "tracks":{
        "track1":"https://mp3.pm/artist/273977/E_Nomine/",
        "track2":"https://mp3.pm/song/106635887/Eros_Ramazzotti_-_Un_Cuore_Con_Le_Ali/",
        "track3":"hhttps://mp3.pm/song/128087875/Kat_Dahlia_-_Gangsta_En_Espa_ol/",
        "track4":"https://mp3.pm/song/84235804/Prince_Royce_-_La_Carretera/",
        "track5":"https://mp3.pm/song/39465561/Xuxa_-_Soco_bate_vira/",
        "track6":"https://mp3.pm/song/569917/Tarkan_-_MashAllah/",
    }
}

class ApiError(code):
    if code == 201:
        pass

new = requests.post('/api/v1/tracks/new', json = newtrack)
if new.status_code != 201:
    raise ApiError('GET /tracks {}'.format(new.status_code))

newplaylist = request.post('/api/v1/playlists/new',newplaylistdata, json = newplaylistdata)
if newplaylist.status_code != 201:
    raise ApiError('POST /new {}'.format(newplaylist.status_code))
