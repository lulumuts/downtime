from flask import render_template, redirect, url_for
from . import auth
from flask_login import login_required
from .. import db
from app.models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register')
def register():
    register = RegistrationForm()
    if register.validate_on_submit():
        new_user = User(name=register.Name.data, email=register.Email.data, phonenumber= register.Phonenumber.data, password=register.Password.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title="New Account"

    return render_template('register.html', title=title, Form=register)