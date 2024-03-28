from app import app

from flask import render_template, url_for, request, redirect
from forms.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app.config['SECRET KEY'] = 'bace1b5adc790cfb9027f100ff9e1478'


@app.route("/")
def index():
    return render_template('public/index.html')

@app.route('/form_view')
def form_view():
    return render_template('public/forms/form_view.html')


@app.route('/about')
def about():
    return render_template('public/templates/about.html')

@app.route('/catalog')
def catalog():
    return render_template('public/templates/catalog.html')

@app.route('/contact')
def contact():
    return render_template('public/templates/contact.html')

@app.route('/measure')
def measure():
    return render_template('public/templates/measure.html')

@app.route('/order')
def order():
    return render_template('public/templates/order.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    return render_template('public/forms/login.html')

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template('public/forms/sign_up.html')

@app.route("/public_form")
def form_view():
    return render_template('public/template/public_form.html')

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
