from . import db
from datetime import datetime

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rating = db.Column(db.Float, default=1500.0)

    def __repr__(self):
        return f"<Subject {self.name} ({self.rating})>"
    

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    winner_id     = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    