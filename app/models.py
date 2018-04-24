from . import db
from datetime import datetime
from twilio.rest import Client

class Events(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer,primary_key = True)
    who = db.Column(db.String(255))
    what = db.Column(db.String(255))
    when = db.Column(db.DateTime,default=datetime.utcnow)
    where = db.Column(db.String(255))
    message = db.Column(db.String(255))


    def save_event(self):
        # Review.all_reviews.append(self)
        db.session.add(self)
        db.session.commit()
