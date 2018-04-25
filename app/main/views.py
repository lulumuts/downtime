from . import main
from flask import render_template,redirect, url_for,request
from .forms import EventsForm,ContactForm
from ..models import Events,Contact
from ..import db
from twilio.rest import Client
import time
import calendar
import datetime

account_sid='AC905360593c371acea0ec4417770b3fd5'
auth_token='d962e83a5a6c92b72a2530e705db61eb'

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/events', methods = ['GET','POST'])
def event():


    form = EventsForm()
    tday = datetime.date.today() #prints out todays date



    if form.validate_on_submit():

        y=int(form.y.data)
        m=int(form.m.data)
        d=int(form.d.data)
        dday = datetime.date(y, m , d)

        till_dday = dday - tday
        x = till_dday.total_seconds()
        while True:
            uin = x
            print(uin)
            try:
                when_to_stop = abs(int(uin))
            except KeyboardInterrupt:
                    break
            except:
                print("Not a number! :P ")

            while when_to_stop >= 0:
                    m, s = divmod(when_to_stop, 60)
                    h, m = divmod(m, 60)
                    d, h = divmod(h, 24)
                    time_left = (str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
                    print(time_left + "\r", end="")
                    time.sleep(1)
                    when_to_stop -= 1

            #if statement: replaces the print statement with the event that was set by the user...
            if  time_left == "00:00:00":
                if form.validate_on_submit():
                    name= form.name.data
                    phone=form.phone.data
                    what=form.what.data
                    where=form.where.data
                    message=form.message.data


                    print("hello")
                    print(phone, message)


                    client = Client(account_sid, auth_token)
                    client.api.account.messages.create(
                    to=form.phone.data,
                    from_="+12522622704",
                    body=form.message.data
                    )

                    new_event=Events(name=name,phone=phone, what=what, y=y,m=m,d=d, where=where,message=message)

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

@main.route('/calendar')
def contact():

    return render_template('calendar.html')

@main.route('/contacts', methods = ['GET','POST'])
def create_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
        name = form.name.data,
        email = form.email.data,
        phone_number = form.phone_number.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('contacts.html', contacts_form=form)
'''

@main.route('/contacts<int:contact_id>')
def view_contact(contact_name):
    contact = Contact.query.filter_by(id=contact_name).first()
    if contact:
        return render_template('contacts.html', contact=contact)
    return 'Contact not found'
'''

'''
@main.route('/contacts<int:contact_id>')
def delete_contact(contact_name):
    contact = Contact.query.get(id=contact_name)

    db.session.delete(contact)
    db.session.commit()

    return render_template('contacts.html')
'''

'''
    message = client.messages.create(to="+254719656398",from_="+12522622704",body=)

    print(message.sid)
'''
