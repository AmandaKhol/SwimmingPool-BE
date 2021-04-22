
from flask import Flask, jsonify
from flask_restful import Resource
from models.street import StreetModel
from centers import centers


class StreetList(Resource):
    def get(self):
        return {'streets': [street.json() for street in StreetModel.query.all()]}, 200

        # hoursInfo = []
        # for center in centers:
        #     if center['id'] == poolId:
        #         pool_info = {
        #             'name': center['name'],
        #             'hours': center['hours']
        #         }
        #         hoursInfo.append(pool_info)
        # return jsonify({'hours': hoursInfo})