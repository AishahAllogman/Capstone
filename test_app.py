import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Capstone"
        self.database_path =  "postgres://{}/{}".format("localhost:5432",self.database_name)
        setup_db(self.app, self.database_path)

        self.moive={
            "id': 101,
            'title': 'Anne',
            'release_data': '5june2016'
        }
        
        self.actor={
            'id':1,
            'name': "sara",
            'age': 30,
            'gender': 'f'
        }

        # binds the app to \the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_reteirve_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_404_if_movies_does_not_exist(self):
        res = self.client().get('/movies/600')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')  
    # Teset : to retrieve_actors      
    def test_retrieve_actors(self):
        res = self.client().get('/actors')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])
       


    def test_404_sent_retrieve_actors_beyond_valid_page(self):
        res = self.client().get('/actors/1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')
    #to delete moives
    def test_delete_movies(self):
       res = self.client().delete('/movies/2')
       data = json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertEqual(data['deleted'], 2)
      

    def test_404_if_movies_does_not_exist(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    # test : to create new moives
    def test_create_moives(self):
        res = self.client().post('/moives',   json=self.new_question)
        data = json.loads(res.data)
        pass
    
    def test_422_if_moives_creation_fails(self):
        res = self.client().post('/moives', json=self.new_question)
        data = json.loads(res.data)
        pass

  
        
    
          


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
