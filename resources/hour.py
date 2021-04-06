import sqlite3

from flask_restful import Resource
from models.hour import HourModel

class HourList(Resource):
    def get(self):
        return {'hours': [hour.json() for hour in HourModel.query.all()]}, 200

