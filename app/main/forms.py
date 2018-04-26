from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,DateField, SubmitField,IntegerField,DateTimeField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required

class EventsForm(FlaskForm):

    name = StringField('Contact', validators=[Required()])
    phone = StringField('Phone /+254719098564/', validators=[Required()])
    what = TextAreaField('Event',validators=[Required()])
    Date = StringField("Enter Date /yyy,mm,dd/:", validators=[Required()])
    Time = StringField("Enter Time: /00:00/", validators=[Required()])
    where = StringField('Location',validators=[Required()])
    message = TextAreaField('Queued message',validators=[Required()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    phone_number = IntegerField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    submit = SubmitField('Submit')
