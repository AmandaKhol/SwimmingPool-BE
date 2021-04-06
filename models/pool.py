import sqlite3
from db import db

class PoolModel(db.Model):
    __tablename__ = 'pools'

    id = db.Column(db.Integer, primary_key=True)
    pool_name = db.Column(db.String(20))
    price = db.Column(db.Float(precision=2))

    #Back reference
    streets = db.relationship('StreetModel')

    def __init__(self, _id, pool_name):
        self.id = _id
        self.pool_name = pool_name
