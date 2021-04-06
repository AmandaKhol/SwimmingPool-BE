import sqlite3
from db import db


class HourModel(db.Model):
    __tablename__ = 'hours'

    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.String)

    # Back reference
    # reservations = db.relationship('ReservationModel')

    def __init__(self,_id, hour):
        self.id = _id
        self.hour = hour

    def json(self):
        return {'id_hour': self.id, 'hour': self.hour}