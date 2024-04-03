from flask import Flask, make_response

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'bace1b5adc790cfb9027f100ff9e1478'

    from .views import bp
    from .auth import auth

    app.register_blueprint(bp, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app


#from app import views
#from app import admin_views