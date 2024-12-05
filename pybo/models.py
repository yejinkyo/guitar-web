
from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="Add a description")

class Order(db.Model):
    o_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('order_set'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Integer, default=datetime.utcnow)

class Post(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, onupdate=datetime.utcnow)
    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    author = db.relationship('User', backref=db.backref('post_set'))



