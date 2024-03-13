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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PWedge = db.Column(db.Integer)
    Nine_Iron = db.Column(db.Integer)
    Eight_Iron = db.Column(db.Integer)
    Seven_Iron = db.Column(db.Integer)
    Six_Iron = db.Column(db.Integer)
    Five_Iron = db.Column(db.Integer)
    Four_Iron = db.Column(db.Integer)
    Three_Iron = db.Column(db.Integer)
    Hybrid = db.Column(db.Integer)
    Five_Wood = db.Column(db.Integer)
    Three_Wood = db.Column(db.Integer)
    Driver = db.Column(db.Integer)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

    
class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
