from flask import Blueprint
#from app import app

from flask import render_template, url_for, request, redirect, jsonify
#from forms.forms import RegistrationForm, LoginForm
#from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import InputRequired, Length, ValidationError
from .models import Order
from . import db
import json

bp = Blueprint("views", __name__)
#app.config['SECRET KEY'] = 'bace1b5adc790cfb9027f100ff9e1478'
@bp.after_request
def add_no_cache(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@bp.route("/")
def index():
    return render_template('public/index.html', user=current_user)

@bp.route('/about')
def about():
    return render_template('public/about.html')

@bp.route('/catalog')
def catalog():
    return render_template('public/catalog.html')

@bp.route('/contact')
def contact():
    return render_template('templates/public/contact.html')

@bp.route('/measure')
def measure():
    return render_template('public/measure.html')

@bp.route('/order')
def order():
    return render_template('public/order.html')



"""
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('forms/template/register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('forms/template/login.html', title='Login', form=form)
"""
