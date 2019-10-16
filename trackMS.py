
import flask_api
import sys
from flask_api import status, exceptions, FlaskAPI
from flask import request, jsonify, g, url_for

import sqlite3



app = FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.commit()
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv



@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('music.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
# method that takes provided dict args 
# and return key=value for each element of
# track table with AND in between

def create_tracks_Query(args):
    q_args=[]
    query=''
    title = args.get('title')
    artist = args.get('artist')
    loc = args.get('link')
    len = args.get('length')
    art = args.get('artwork')
    if title:
        query +=" title=? AND"
        q_args.append(title)
    
    if artist:
        query+=" artist=? AND"
        q_args.append(artist)
    
    if loc:
        query+=" link=? AND"
        q_args.append(loc)
    
   
    if len:
               
        query+=" length=? AND"
        q_args.append(len)
      
    if art:
        query += " artwork=? AND"
        q_args.append(art)
    if not (title or len or artist or art or loc):
        raise exceptions.NotFound()
    query = query[:-4]
    return (query, q_args)



#TODO place holder method to be changed later
@app.route('/', methods=['GET'])   
def default():
    return '''<h1>Place Holder<h1>'''


# method that decides whehter request is
# to get specified track based on vars passed through url 
# or to add new song
@app.route('/api/v1/tracks', methods=['GET', 'POST', 'DELETE'])
def tracks():
    """
    find or edit songs
    """
    if request.method == 'GET':
        return find_song(request.args)
    elif request.method == 'POST':
        return edit_song(request.args, request.data)
    elif request.method == 'DELETE':
        return delete_song(request.args)

#takes arguments from url and use to construct a query to
#find songs matching the specifications given
def find_song(args):
    
    temp, q_args = create_tracks_Query(args)
    query = "SELECT * FROM tracks WHERE"
    query += temp + ";"
    ret_tracks=query_db(query, q_args)
    if ret_tracks:
        return ret_tracks
    else:
        raise exceptions.NotFound()


def edit_song(args, data):
    q_args=[]
    query="UPDATE tracks SET "
    temp, q_args=create_tracks_Query(data)
    temp=temp.replace(' AND',',')
    query+=temp +' WHERE'
    temp, temp_args=create_tracks_Query(args)
    query+=temp+ ';'
    q_args.extend(temp_args)    
    query_db(query, q_args)
    query = "SELECT * FROM tracks WHERE"
    query+=temp+';'
    
    return {"Message":"Content Sucessfully updated"}, status.HTTP_201_CREATED

def delete_song(args):
    temp, q_args = create_tracks_Query(args)
    query = "DELETE FROM tracks WHERE"
    query += temp + ";"
    query_db(query, q_args)
    query = "SELECT * FROM tracks WHERE"+ temp + ";"
    ret_tracks=query_db(query, q_args)
    
    if ret_tracks:
        return ret_tracks, status.HTTP_417_EXPECTATION_FAILED
    else:
        return {"Message":"Content Sucessfully Deleted"}, status.HTTP_200_OK

@app.route('/api/v1/tracks/new', methods=['POST', 'GET'])
def new_song():
    if request.method =='POST':

        required=['title', 'artist', 'length', 'link']
        if not all([fields in request.data for fields in required]):
            raise exceptions.ParseError()

        temp , q_args = create_tracks_Query(request.data)
        query = "Insert into tracks(title, artist, length, link, artwork) VALUES(?,?,?,?,?);"
        art = request.data.get("artwork")
        if  art: 
            pass
        else:
            q_args.append("HTTPS:\\Default\Art")

         

        try:
            query_db(query, q_args)
        except Exception as e:
            return {'error': str(e)}, status.HTTP_409_CONFLICT
        
        return request.data, status.HTTP_201_CREATED
    else:
       
        return  {"INFO":"Enter Data For New Track"}, status.HTTP_200_OK

#test posts


# {
#     "title":"Free Fallin",
#     "artist":"Tom Petty",
#     "length":"3:00",
#     "link":"C://music//tom//Free",
#     "artwork":"https://art/cool/pic"

    
# }
        
    # {"title":"Yester", "length":"3:00"}

    # {"title":"Yesterday"}
    # {"title": "PaperBack Writer", "artist":"The Beetles"}


