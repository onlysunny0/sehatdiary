from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    hemoglobiny = db.Column(db.String(150))
    tlc = db.Column(db.Integer)
    platelets = db.Column(db.Integer)
    ers = db.Column(db.Integer)
    bt = db.Column(db.Integer)
    ct = db.Column(db.Integer)
    bloodgroup = db.Column(db.String(150))
    bloodshugar = db.Column(db.Integer)
    bloodurea = db.Column(db.Integer)
    