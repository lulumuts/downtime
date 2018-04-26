from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,DateField, SubmitField,IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    name = StringField('NAME', validators=[Required()])
    phone = StringField('PHONE', validators=[Required()])
    what = TextAreaField('EVENT',validators=[Required()])
    y= IntegerField('YEAR',validators=[Required()])
    m=IntegerField('MONTH',validators=[Required()])
    d=IntegerField('DAY',validators=[Required()])
    where = StringField('WHERE',validators=[Required()])
    message = TextAreaField('MESSAGE',validators=[Required()])
    submit = SubmitField('SUBMIT')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    phone_number = IntegerField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    submit = SubmitField('Submit')
