from flask_script import Manager,Shell,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Events,Contact
from twilio.rest import Client
from app import create_app,db

app = create_app('default')

migrate=Migrate(app,db)
manager = Manager(app)


manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Events = Events, account_sid=account_sid, auth_token=auth_token, Contact = Contact)

if __name__ == '__main__':
    manager.run()
