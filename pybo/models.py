
from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
