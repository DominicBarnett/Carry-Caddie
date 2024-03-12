from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy_utils import URLType
from flask_login import UserMixin
from GolfCarry_App import db
from GolfCarry_App.utils import FormEnum

class ProAverageCategory(FormEnum):
    """Pro Average Carry numbers"""
    Driver = 275
    Three_Wood = 243
    Five_Wood = 230
    Hybrid = 225
    Three_Iron = 212
    Four_Iron = 203
    Five_Iron = 194
    Six_Iron = 183
    Seven_Iron = 172
    Eight_Iron = 160
    Nine_Iron = 148
    PWedge = 136

class CarryYardages(db.Model):
    """Affiliation model. What group a given created character is apart of"""
    id = db.Column(db.Integer, primary_key=True)
    PWedge = db.Column(db.Integer, primary_key=True)
    Nine_Iron = db.Column(db.Integer, primary_key=True)
    Eight_Iron = db.Column(db.Integer, primary_key=True)
    Seven_Iron = db.Column(db.Integer, primary_key=True)
    Six_Iron = db.Column(db.Integer, primary_key=True)
    Five_Iron = db.Column(db.Integer, primary_key=True)
    Four_Iron = db.Column(db.Integer, primary_key=True)
    Three_Iron = db.Column(db.Integer, primary_key=True)
    Hybrid = db.Column(db.Integer, primary_key=True)
    Five_Wood = db.Column(db.Integer, primary_key=True)
    Three_Wood = db.Column(db.Integer, primary_key=True)
    Driver = db.Column(db.Integer, primary_key=True)
    created_by = db.relationship('User')

    def __str__(self):
        return self.affiliation_name

    def __repr__(self):
        return self.affiliation_name
    
class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
