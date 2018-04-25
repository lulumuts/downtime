from . import db
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
