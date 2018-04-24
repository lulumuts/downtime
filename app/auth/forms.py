from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    Email = StringField("Email", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField('Remembe me')
    Submit= SubmitField('Login')



def validate_email(form, data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError('This email already exists')
    

def validate_phonenumber(form, data_field):
    if User.query.filter_by(phonenumber= data_field.data).first():
        raise ValidationError('This number already exists')


class RegistrationForm(FlaskForm):
    Name = StringField('Name', validators=[Required()])
    
    Email = StringField('Email', validators=[Required(), Email(), validate_email])
    Phonenumber = StringField('Phone Number', validators=[Required(), validate_phonenumber])
    Password = PasswordField("Password", validators=[Required(),
    EqualTo('password_confirm', message=' Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')


