from flask import render_template, redirect, url_for, request, flash
from . import auth
from flask_login import login_required, login_user, logout_user, current_user
from .. import db
from app.models import User
from .forms import LoginForm, RegistrationForm
from .. import login_manager
from flask_login import UserMixin




@auth.route('/login', methods=['POST', 'GET'])
def login():
    title= "Downtime | Login"
    Login = LoginForm()
    if Login.validate_on_submit():
        user = User.query.filter_by(email=Login.Email.data).first()
        if user is not None and user.verify_password(Login.password.data):
            login_user(user, Login.remember_me.data)
<<<<<<< HEAD
            return redirect(request.args.get('next') or url_for('main.index'))
=======
            return redirect(request.args.get('next') or url_for('auth.register'))
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050
        flash("Either username or email invalid")

    return render_template('auth/login.html', title=title, Login=Login)




@auth.route('/register', methods = ['GET', 'POST'])
def register():
    register = RegistrationForm()
<<<<<<< HEAD

=======
    
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050
    if register.validate_on_submit():
        new_user = User(username=register.Name.data, email=register.Email.data, phonenumber= register.Phonenumber.data, password=register.Password.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
<<<<<<< HEAD



    title="Downtime | New Account"

    return render_template('auth/register.html', title=title, Form=register)
=======
    
        

    title="Downtime | New Account"

    return render_template('auth/register.html', title=title, Form=register)
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050
