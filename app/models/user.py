from enum import EnumMeta
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users' 
    __table_args__ = tuple(db.UniqueConstraint(
        'id', 'username', name='my_2uniq'))

    id = db.Column(db.String(), primary_key=True, unique=True)
    username = db.Column(db.String(), primary_key=True)
    lastname = db.Column(db.String())
    firstname = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, username, api_key, firstname, lastname, email, password):

        self.id = id
        self.username = username
        self.api_key = api_key
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'first_name': self.firstname,
            'last_name': self.lastname,
            'email': self.email,
            'password': self.password,
            'api_key': self.api_key
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self