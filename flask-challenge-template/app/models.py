from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .init_app import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(121), nullable=False)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(121), nullable=False)
    stadium_id = db.Column(db.Integer, db.ForeignKey('stadium.id'), nullable=False)
    stadium = db.relationship('Stadium', backref=db.backref('matches', lazy=True))
    start_at = db.Column(db.DateTime, nullable=False)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    match = db.relationship('Match', backref=db.backref('seats', lazy=True))
    user_id = db.Column(db.Integer, nullable=True) 
    location = db.Column(db.Integer, nullable=False)
    reserved_at = db.Column(db.DateTime, nullable=True)
