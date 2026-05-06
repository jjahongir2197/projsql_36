from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

@event.listens_for(User, 'after_insert')
def after_user_insert(mapper, connection, target):
    print(f"New user added: {target.username}")

with app.app_context():
    db.create_all()

    u = User(username="Jahongir")
    db.session.add(u)
    db.session.commit()
