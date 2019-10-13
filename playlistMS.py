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
        with app.open_resource('songs.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
def createQuery(args):
    user=args.get(creator)
    title=args.get(title)
    descripton=args.get(description)
    qargs=[]
    query="WHERE"
    
    if user:
        query+=" CREATOR=? AND"
        qargs.append(user)

    if title:
        query+=" TITLE=? AND"
        qargs.append(title)
    
    if description:
        query+=" DESCRIPTION=? AND"
        qargs.append(description)

    
    query=query[:-4]
    return query, qargs

@app.route('/')
def default():
    return "<h1>Placeholder<h1>"


@app.route('/api/v1/playlists', methods=["GET","DELETE"])
def playlists():
    if request.method =='GET':
        return retrieve(request.args)
    else:
        return delete(request.args)

#TODO
def retrieve(args):
    s_query, s_qargs= createQuery(args)
    s_query= "SELECT * FROM playlists "+ s_query
    if len(s_qargs) == 0:
        return {"MESASGE":'Please enter values to search for'}, status.HTTP_404_NOT_FOUND
    
    try:
        result = query_db(s_query, s_qargs)
    except Exception as e:
            return {'error': str(e)}, status.HTTP_404_NOT_FOUND
    
    for x in result:
        id = x.get(id)
        if not id:
            raise exceptions.NotFound()

        query= "SELECT track_url FROM playlist_tracks WHERE playlist_id=?"
        qargs=[id]
        tracks= query_db(query, qargs)
        x.update({"tracks":tracks}) 

    return result, status.HTTP_200_OKAY 



#TODO Test delete
def delete(args):
    
    s_query, s_qargs= createQuery(args)
    if len(s_qargs)==0:
        return {"MESSAGE":"PLEASE SPECIFY PLAYLST"}, status.HTTP_404_NOT_FOUND
    s_query='SELECT id FROM playlists' + s_query
    d_query="DELETE FROM playlist_tracks WHERE plalist_id IN ("+s_query+')'
    query_db(d_query, s_qargs)

    d_query=s_query.relplace("SELECT id", "DELETE")
    query_db(d_query, s_qargs)

    return {'MESSAGE':'Playlist deleted'}, status.HTTP_200_OKAY


#TODO
@app.route('/api/v1/playlists/all', methods=["GET"])
def all_playlists():
    pass

#TODO
@app.route('/api/v1/playlists/<user>', methods=['GET'])
def user_playlists():
    pass