from sqlalchemy.sql import func
from config import db


class Dojo(db.Model):
    __tablename__ = "dojos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())


class Ninja(db.Model):
    __tablename__ = "ninjas"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(
        db.Integer, db.ForeignKey("dojos.id"), nullable=False)
    dojo = db.relationship('Dojo', foreign_keys=[
        dojo_id], backref="ninjas", cascade="all")
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())
