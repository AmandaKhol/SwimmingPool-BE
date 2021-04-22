
from flask import Flask, jsonify
from flask_restful import Resource
from models.hour import HourModel
from centers import centers


class HourList(Resource):
    def get(self):
        return {'hours': [hour.json() for hour in HourModel.query.all()]}, 200

        # hoursInfo = []
        # for center in centers:
        #     if center['id'] == poolId:
        #         pool_info = {
        #             'name': center['name'],
        #             'hours': center['hours']
        #         }
        #         hoursInfo.append(pool_info)
        # return jsonify({'hours': hoursInfo})