
from flask import Flask, jsonify
from flask_restful import Resource
from centers import centers

from models.pool import PoolModel

class Pool(Resource):
    def get(self, pool_id):
        pool = PoolModel.find_by_id(pool_id)
        if pool:
            return pool.json(), 200
        return {'message': 'Item not found'}, 404


class PoolList(Resource):
    def get(self):
        return {'pools': list(map(lambda x: x.json(), PoolModel.query.all()))}
        # return {'pools': [pool.json() for pool in PoolModel.query.all()]}, 200
        # pools = []
        # for center in centers:
        #     pools.append(center['name'])
        # return jsonify({'pools': pools})

