import flask
import flask_api
import sys
from flask_api import status, exceptions
from flask import request, jsonify, g
import sqlite3


app = flask.Flask(__name__)
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
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(insert, args=()):
    cur = get_db().execute(insert, args)
    cur.close()

@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('songs.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


#TODO place holder method to be changed later
@app.route('/', methods=['GET'])   
def default():
    return '''<h1>Place Holder<h1>'''

#method that decides whehter request is
# to get specified track based on vars passed through url 
# or to add new song
@app.route('/v1/tracks', methods=['GET', 'POST'])
def tracks():
    if request.method == 'GET':
        return find_song(request.args)
    elif request.method == 'POST':
        return add_song(request.data)

#takes arguments from url and use to construct a query to 
#find songs matching the specifications given
def find_song(args):
    title = args.get('title')
    artist = args.get('artist')
    loc = args.get('link')
    len = args.get('len')
    art = args.get('artwork')

    query="SELECT * FROM tracks WHERE"
    q_args=[]

    if title:
        query +=" title=? AND"
        q_args.append(title)
    
    if artist:
        query+=" artist=? AND"
        q_args.append(artist)
    
    if loc:
        query+=" link=? AND"
        q_args.append(loc)
    
    #can optionally specify a comparson symbol at end of variable
    # defaults to = 
    # times must be entered in MM:SS format with leading zeros,
    # minutes and seonds must not exceed 59
    # if times are to exceed 1hour then errors may occur
    if len:
        op='='
        symbs="=<>"
        if len[-1] in symbs:
            op=len[-1]
            len=len[:-1]
        query+=" time(length)" + op + "time(?) AND"
        q_args.append(len)

    if art:
        query += " artwork=? AND"
        q_args.append(art)

    query = query[:-4] + ';'

    return jsonify(query_db(query, q_args))



