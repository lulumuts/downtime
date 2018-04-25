from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,DateField, SubmitField,IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    name = StringField('contact', validators=[Required()])
    phone = StringField('phone', validators=[Required()])
    what = TextAreaField('event',validators=[Required()])
    y= IntegerField('year',validators=[Required()])
    m=IntegerField('month',validators=[Required()])
    d=IntegerField('day',validators=[Required()])
    where = StringField('location',validators=[Required()])
    message = TextAreaField('queued message',validators=[Required()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    phone_number = IntegerField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    submit = SubmitField('Submit')
