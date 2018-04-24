from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    who = StringField('contact', validators=[Required()])
    what = TextAreaField('event',validators=[Required()])
    when= StringField('time',validators=[Required()])
    where = StringField('location',validators=[Required()])
    message = TextAreaField('queued message',validators=[Required()])
    submit = SubmitField('Submit')
