from app import app

from flask import render_template, url_for, request, redirect
#from forms.forms import RegistrationForm, LoginForm
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import InputRequired, Length, ValidationError


@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/profile')
def admin_profile():
    return "Admin profile"