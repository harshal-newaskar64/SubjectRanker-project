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
    winner_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        # show the first 20 chars of text for brevity
        snippet = (self.text[:20] + '…') if len(self.text) > 20 else self.text
        return f"<Feedback {self.id} by {self.username}: \"{snippet}\">"
