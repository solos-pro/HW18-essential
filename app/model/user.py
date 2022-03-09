from marshmallow import Schema, fields
from app.database import db


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, unique=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role_id = db.Column(db.String, db.ForeignKey("group.id"))
    role = db.relationship("Group")


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str(load_only=True)
    role = fields.Str()


class GroupSchema(Schema):
    id = fields.Int()
    role = fields.Str()
