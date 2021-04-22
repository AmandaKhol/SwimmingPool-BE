import sqlite3
from db import db


class HourModel(db.Model):
    __tablename__ = 'hours'

    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.String)

    # pool_id = db.Column(db.String, db.ForeignKey('pools.id'))
    # pool = db.relationship('PoolModel')


    def __init__(self, hour):
        self.hour = hour

    def json(self):
        return {'id_hour': self.id, 'hour': self.hour}