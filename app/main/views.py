from . import main
from flask import render_template,redirect, url_for
from .forms import EventsForm
from ..import db

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/events', methods = ["GET","POST"])
def event():

    form = EventsForm()

    if form.validate_on_submit():
        who= form.who.data
        what=form.what.data
        when=form.when.data
        where=form.where.data
        message=form.message.data

        new_event=Events(who=who, what=what, when=when, where=where,message=message)

        new_event.save_event()
        return redirect(url_for('.index'))

    return render_template('events.html', events_form=form)
