from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Events,Contact
from twilio.rest import Client
from app import create_app,db
from app.models import User
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')
app.app_context().push()

migrate=Migrate(app,db)
manager = Manager(app)


manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Events = Events, User=User)


if __name__ == '__main__':
    manager.run()
