from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    coldplay = Artist(name='Edward Hartono', about='MIS')
    maroon5 = Artist(name='Mark Serva', about='MIS')
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
