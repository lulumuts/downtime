from . import main
from flask import render_template,redirect, url_for,request
from .forms import EventsForm
from ..models import Events
from ..import db
from twilio.rest import Client

account_sid='AC905360593c371acea0ec4417770b3fd5'
auth_token='d962e83a5a6c92b72a2530e705db61eb'

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/events', methods = ['GET','POST'])
def event():
    client = Client(account_sid, auth_token)
    form = EventsForm()

    if form.validate_on_submit():
        who= form.who.data
        what=form.what.data
        when=form.when.data
        where=form.where.data
        message=form.message.data

        client = Client(account_sid, auth_token)
        client.api.account.messages.create(
        to="+254727481326",
        from_="+12522622704",
        body=form.message.data
        )

        new_event=Events(who=who, what=what, when=when, where=where,message=message)

        new_event.save_event()
        return redirect(url_for('.index'))

    return render_template('events.html', events_form=form,message=form)

@main.route('/send',methods=['POST'])
def send():

    send = EventsForm()

    if send.validate_on_submit():
        when = send.when.data
        message = form.message.data
        print("hello")
        print(when, message)

        client.api.account.messages.create(
        to="+254727481326",
        from_="+12522622704",
        body=send.message.data
        )
        return redirect(url_for('main.index'))



    return render_template('index.html', message=send)

    '''
    message = client.messages.create(to="+254719656398",from_="+12522622704",body=)

    print(message.sid)
    '''
