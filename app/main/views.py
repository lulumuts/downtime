from  . import main
from flask import render_template,redirect, url_for,request,flash
from .forms import EventsForm,ContactForm
from ..models import Events,Contact
from ..import db
from twilio.rest import Client
import time
import calendar
import datetime
import pytz
from threading import Thread

account_sid = None
auth_token = None

def configure_views(app):
    global account_sid,auth_token

    account_sid= app.config['ACCOUNT_SID']
    auth_token = app.config['AUTH_TOKEN']

def send_sms(to,body,dday):
    tday = datetime.datetime.now() #prints out todays date

    print(tday)
    print(dday)

    till_dday = dday - tday
    x = till_dday.total_seconds()-10800
    while True:
        print(x)
        try:
            when_to_stop = abs(int(x))
            print(when_to_stop)
        except KeyboardInterrupt:
                break
        except:
            print("Not a number! :P ")
        while when_to_stop >= 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)
            time_left = (str(d).zfill(2) + " " + str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
            print(time_left + "\r", end="")
            time.sleep(1)
            when_to_stop -= 1

            #if statement: replaces the print statement with the event that was set by the user...
            if  time_left == "00 00:00:00":
                client = Client(account_sid, auth_token)
                client.api.account.messages.create(
                to=to,
                from_="+12243850267",
                body=body
                )
                return
        break

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/events', methods = ['GET','POST'])
def event():
    try:

        form = EventsForm()




        if form.validate_on_submit():
            duedate=form.Date.data
            dtime= form.Time.data
            year, month, day = map(int, duedate.split(','))
            hour, minute = map(int, dtime.split(':'))
            dday = datetime.datetime(year, month, day, hour, minute)


            name= form.name.data
            phone=form.phone.data
            what=form.what.data
            where=form.where.data
            message=form.message.data


            print("hello")
            print(phone, message)

            thr = Thread(target=send_sms,args=[phone,message,dday])
            thr.start()


            new_event=Events(name=name,phone=phone, what=what,time=dtime,date=duedate ,where=where,message=message)

            new_event.save_event()
            return redirect(url_for('.index'))

        return render_template('events.html', events_form=form,message=form)
    except:
        flash('Please use the correct phone number, date and time format!')
        return redirect(url_for('.event'))

@main.route('/calendar')
def contact():

    return render_template('calendar.html')

@main.route('/display')
def display():
    events = Events.query.all()
    return render_template('display.html',events=events)
