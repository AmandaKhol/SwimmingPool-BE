import sqlite3
from db import db


class StreetModel(db.Model):
    __tablename__ = 'streets'

    id = db.Column(db.Integer, primary_key=True)
    max_swimmers = db.Column(db.Integer)

    pool = db.Column(db.Integer, db.ForeignKey('pool.id'))

    # Back reference
    reservations = db.relationship('ReservationModel')

    def __init__(self,_id, max_swimmers):
        self.id = _id
        self.max_swimmers = max_swimmers

