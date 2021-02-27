import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, rsources={r"/app/*": {"origins": "*"}})

    return app


app = create_app()


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization,true')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET,PUT,POST,DELETE,OPTIONS')
    return response
# GEt Moives for server after authentication :


@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def reteirve_movies(payload):
    Movies = Movie.query.all()
    movies = [movie.format()for movie in Movies]

    return jsonify({
        'success': True,
        'movies': movies
    })
# Post 'add' Moives to server after authentication :


@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movies(payload):
    body = request.get_json()
    req_id = body.get('id')
    req_title = body.get('title')
    req_releasedata = body.get('release_data')
    try:
        movie = Movie(id=req_id, title=req_title, release_data=req_releasedata)
        movie.insert()
        return jsonify({
            'success': True,
            'movie': [movie.format()]
        })
    except Exception as e:
        print(e)
        abort(422)
# Patch  'edit' Moives to server after authentication :


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movies(payload, movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)
    body = request.get_json()
    req_title = body.get('title')
    req_releasedata = body.get('release_data')
    try:
        movie.title = req_title
        movie.release_data = req_releasedata
        movie.update()

        return jsonify({
            'success': True,
            'movie': [movie.format()]

        })
    except Exception as e:
        print(e)
        abort(422)
# Delete Moives from  server after authentication :


@app.route('/movies/<int:movies_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(payload, movies_id):
    Movies = Movie.query.filter(Movie.id == movies_id).one_or_none()
    if Movies is None:
        abort(404)
    try:
        Movies.delete()
        return jsonify({
            'success': True,
            'detele': movies_id
        })
    except Exception as e:
        print(e)
        abort(422)

# GEt Moives for server after authentication :


@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def reteirve_actors(payload):
    Actors = Actor.query.all()
    actors = [actor.format()for actor in Actors]

    return jsonify({
        'success': True,
        'actors': actors
    })

# Post 'add' Actors to server after authentication :


@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actors(payload):
    body = request.get_json()
    req_id = body.get('id')
    req_name = body.get('name')
    req_age = body.get('age')
    req_gender = body.get('gender')
    try:
        actor = Actor(id=req_id, name=req_name, age=req_age, gender=req_gender)
        actor .insert()
        return jsonify({
            'success': True,
            'actor': [actor .format()]
        })
    except Exception as e:
        print(e)
        abort(422)

# Patch  'edit' Actors  to server after authentication :


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actors(payload, actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)
    body = request.get_json()
    req_title = body.get('title')
    req_name = body.get('name')
    req_gender = body.get('gender')
    try:
        actor.name = req_name
        actor.gender = req_gender
        actor.update()

        return jsonify({
            'success': True,
            'actor': [actor.format()]

        })
    except Exception as e:
        print(e)
        abort(422)
# Delete Actors from  server after authentication :


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(payload, actor_id):
    actors = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actors is None:
        abort(404)
    try:
        actors.delete()
        return jsonify({
            'success': True,
            'detele': actor_id
        })
    except Exception as e:
        print(e)
        abort(422)
# Errorhandler:


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
