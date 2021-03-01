import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "Capstone"
# database_path = '"postgres://{}:{}@{}/{}".format(
# "aisha", "Aisha", "localhost:5432", database_name)'
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
# Movies Class:


class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    release_data = db.Column(db.DateTime())

    def __init__(self, id, title, release_data):
        self.id = id
        self.title = title
        self.release_data = release_data

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_data': self.release_data

        }

# Actors class :


class Actor(db.Model):
    __tablename__ = 'Actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
