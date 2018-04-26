from flask_script import Manager,Shell,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Events,Contact
from twilio.rest import Client
from app import create_app,db
from app.models import User
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
app.app_context().push()

migrate=Migrate(app,db)
manager = Manager(app)


manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Events = Events, account_sid=account_sid, auth_token=auth_token, Contact = Contact)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    manager.run()
