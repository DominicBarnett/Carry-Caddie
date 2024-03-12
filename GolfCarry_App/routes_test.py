from dotenv import load_dotenv
load_dotenv()
import os
import unittest
from flask import Flask
from GolfCarry_App.main.routes import main
from GolfCarry_App.models import User
from GolfCarry_App import app, db, bcrypt

def create_user():
        # Creates a user with username 'me1' and password of 'password'
        password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='test_user', password=password_hash)
        db.session.add(user)
        db.session.commit()

class MainTests(unittest.TestCase):
    def setUp(self):
        """Executed prior to each test."""
        app.config['FLASK_APP'] = 'app.py'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()


    
    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_new_affiliation(self):
        response = self.app.post('/new_affiliation', data=dict(title='New Affiliation'), follow_redirects=True)
        assert response.status_code == 200


    def test_new_character(self):
        response = self.app.post('/new_character', data=dict(name='New Character', category='Pirate', affiliation='Straw Hat Pirates', devil_fruit='No', haki='Yes'), follow_redirects=True)
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
