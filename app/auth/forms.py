from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtfforms import validationError


class LoginForm(FlaskForm):
    Email = StringField("Email", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    Submit= SubmitField('Login Field')


class RegistrationForm(FlaskForm):
    Name = StringField('Name', validators=[Required()])
    Email = StringField('Email', validators=[Required(), Email()])
    Phonenumber = StringField('Phone Number', validators=[Required()])
    Password = PasswordField("Password", validators=[Required(),
    EqualTo('password_confirm', message=' Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign UP')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise validationError('There is an account with that email')
    
    def validate_username(self, data_field):
        if User.query.filter_by(username= data_field.data).first():
            raise validationError('This username already exists')
