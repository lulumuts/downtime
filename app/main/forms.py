from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,DateField, SubmitField,IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    who = StringField('contact', validators=[Required()])
    what = TextAreaField('event',validators=[Required()])
    when= DateField('entrydate',format='%Y-%m-%d')
    where = StringField('location',validators=[Required()])
    message = TextAreaField('queued message',validators=[Required()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    phone_number = IntegerField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    event_id = StringField('Event', validators=[Required()])
    submit = SubmitField('Submit')
