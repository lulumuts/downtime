from . import main
from flask import render_template, redirect, url_for, request, flash
from . import main
from flask_login import login_required, login_user, logout_user, current_user
from .. import db
from app.models import User
from .forms import TextForm
from flask_login import UserMixin
from twilio.rest import Client
from .forms import TextForm
import time
import calendar
import datetime
​
​
​
account_sid=None
auth_token =None
 
​
def configure_views(app):
  global account_sid,auth_token
​
  account_sid = app.config['ACCOUNT_SID']
  auth_token = app.config['AUTH_TOKEN']
​
​
@main.route('/', methods=['POST', 'GET'])
def index():
  Text = TextForm()
  tday = datetime.date.today() #prints out todays date
  
  
  
  
  if Text.validate_on_submit():
    y=int(Text.year.data) 
    m=int(Text.month.data) 
    d=int(Text.day.data) 
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
​
      while when_to_stop >= 0:
          m, s = divmod(when_to_stop, 60)
          h, m = divmod(m, 60)
          d, h = divmod(h, 24)  
          time_left = (str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
          print(time_left + "\r", end="")
          time.sleep(1)
          when_to_stop -= 1
​
      #if statement: replaces the print statement with the event that was set by the user...
      if time_left == "00:00:00":
        if Text.validate_on_submit():
          Number = Text.Number.data 
          Message = Text.Message.data
          print("hello")
          print(Number, Message)
          client = Client(account_sid, auth_token)
          client.api.account.messages.create(
          to=Text.Number.data ,
          from_="+447480487894" ,
          body=Text.Message.data
          )
          redirect(url_for('main.')) 
​
          
​
          print("Done") 
          print("Send Happy bithday message to John Doe!!!")
          print("After break")
​
          break
        
    
​
  return render_template('index.html', message=Text)