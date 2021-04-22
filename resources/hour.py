
from flask import Flask, jsonify
from flask_restful import Resource
from centers import centers


class HourList(Resource):
    def get(self, poolId):
        hoursInfo = []
        for center in centers:
            if center['id'] == poolId:
                pool_info = {
                    'name': center['name'],
                    'hours': center['hours']
                }
                hoursInfo.append(pool_info)
        return jsonify({'hours': hoursInfo})