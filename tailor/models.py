from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dress_type = db.Column(db.String(100))
    fabric_type = db.Column(db.String(100))
    material_type = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    material_unit_cost = db.Column(db.Float)
    total_cost = db.Column(db.Float) 
    date = db.Column(db.DateTime(timezone=True), default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship('User', backref='orders') 


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(6))
    address = db.Column(db.String(250))
    address2 = db.Column(db.String(250))
    city = db.Column(db.String(30))
    country = db.Column(db.String(30))
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    #order = db.relationship('Order')
    orders = db.relationship('Order', backref='user', lazy=True) 

