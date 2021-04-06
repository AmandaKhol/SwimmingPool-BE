import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_card = db.Column(db.String(20))
    max_reservations = db.Column(db.Integer)

    # Back reference
    reservations = db.relationship('ReservationModel')


    def __init__(self,_id, user_card, max_reservations):
        self.id = _id
        self.user_card = user_card
        self.max_reservations = max_reservations


