from . import db
<<<<<<< HEAD
from datetime import datetime
from twilio.rest import Client



class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key = True)
    phone_number = db.Column(db.Integer, unique = True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String, unique = True, index = True)


class Events(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255))
    phone = db.Column(db.String(255))
    what = db.Column(db.String(255))
    y = db.Column(db.Integer)
    m = db.Column(db.Integer)
    d = db.Column(db.Integer)
    where = db.Column(db.String(255))
    message = db.Column(db.String(255))


    def save_event(self):
        # Review.all_reviews.append(self)
        db.session.add(self)
        db.session.commit()
=======
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User( UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phonenumber = db.Column(db.String, unique=True)
    pass_secure = db.Column(db.String)
    
    @property
    def password(self):
        raise AttributeError('You cannot read password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User{self.username}'

    
    
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050
