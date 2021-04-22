import sqlite3
from db import db

class StreetModel(db.Model):
    __tablename__ = 'streets'

    id = db.Column(db.Integer, primary_key=True)

    #Back reference
    pool_id = db.Column(db.String, db.ForeignKey('pools.id'))
    pool = db.relationship('PoolModel')


    def __init__(self, _id, pool_id):
        self.id = _id
        self.pool_id = pool_id

    def json(self):
        return {'id': self.id, 'pool_id': self.pool_id}
