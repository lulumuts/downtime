from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,DateField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    who = StringField('contact', validators=[Required()])
    what = TextAreaField('event',validators=[Required()])
    when= DateField('entrydate',format='%Y-%m-%d')
    where = StringField('location',validators=[Required()])
    message = TextAreaField('queued message',validators=[Required()])
    submit = SubmitField('Submit')
