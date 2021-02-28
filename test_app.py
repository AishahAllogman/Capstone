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

        self.movie={
            "id': 101,
            'title': 'Anne',
            'release_data': '5june2016'
        }
         self.updatemovie={
            'title': 'homealone',
            'release_data': '5june2016'
        }
        
        self.actor={
            'id':1,
            'name': "sara",
            'age': 30,
            'gender': 'f'
        }
        self.updateactor={
            'name': "abrar",
            'age': 20,
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
        res = self.client().get('/movies',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_404_if_movies_does_not_exist(self):
        res = self.client().get('/movies/600',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')  
    # Teset : to retrieve_actors      
    def test_retrieve_actors(self):
        res = self.client().get('/actors',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])
       


    def test_404_sent_retrieve_actors_beyond_valid_page(self):
        res = self.client().get('/actors/1000',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')
    #to delete movies
    def test_delete_movies(self):
       res = self.client().delete('/movies/2',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
       data = json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertEqual(data['deleted'], 2)
      

    def test_404_if_movies_does_not_exist(self):
        res = self.client().delete('/movies/1000',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    #to delete actors
    def test_delete_actors(self):
       res = self.client().delete('/actors/2',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
       data = json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertEqual(data['deleted'], 2)
      

    def test_404_if_actors_does_not_exist(self):
        res = self.client().delete('/actors/1000',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    # test : to create new moives
    def test_create_movies(self):
        res = self.client().post('/movies',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),   json=self.new_movie)
        data = json.loads(res.data)
        pass
    
    def test_422_if_movies_creation_fails(self):
        res = self.client().post('/movies',headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }), json=self.new_new_movie)
        data = json.loads(res.data)
        pass
    # test : to create new  actors 
    def test_create_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),  json=self.new_actor)
        data = json.loads(res.data)
        pass
    
    def test_422_if_actors_creation_fails(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),json=self.new_actors)
        data = json.loads(res.data)
        pass
    # test : to update  movies 
    def test_update_movies(self):
        res = self.client().patch('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),  json=self.updatemovie)
        data = json.loads(res.data)
        pass
    
    def test_422_if_update_movies_fails(self):
        res = self.client().patch('/movies/300', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),  json=self.updatemovie)
        data = json.loads(res.data)
        pass
     # test : to update  movies 
    def test_update_movies(self):
        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),  json=self.updateactors)
        data = json.loads(res.data)
        pass
    
    def test_422_if_update_actors_fails(self):
        res = self.client().patch('/actors/300', headers={
            'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)
        }),  json=self.updateactors)
        data = json.loads(res.data)
        pass
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
