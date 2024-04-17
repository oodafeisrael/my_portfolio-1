from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from tailor import create_app, db 


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    #app.config['DEBUG'] = True
    #app.config['SECRET KEY'] = 'bace1b5adc790cfb9027f100ff9e1478'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' '@localhost/DB_NAME'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:' '@localhost/{DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:' '@localhost/{DB_NAME}"
    #app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://root:' '@localhost/{DB_NAME}"
    #app.config{'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    from .views import bp
    from .auth import auth

    app.register_blueprint(bp, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Order
    
    return app

def create_database(app):
    with app.app_context():
        if not path.exists('tailor/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database!') 


#from app import views
#from app import admin_views