import sqlite3
from db import db


class ReservationModel(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)


    user_id = db.Column(db.Integet, db.ForeignKey('user.id'))
    street_id = db.Column(db.Integet, db.ForeignKey('street.id'))
    hour_id = db.Column(db.Integet, db.ForeignKey('hour.id'))

    user = db.relationship('UserModel')
    street = db.relationship('StreetModel')
    hour = db.relationship('HourModel')

    def __init__(self,_id, date):
        self.id = _id
        self.date = date
