
from flask import Flask, jsonify
from flask_restful import Resource,reqparse
from centers import centers

from models.pool import PoolModel
from models.street import StreetModel

class Pool(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pool_id',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    def get(self, name):
        pool = PoolModel.find_by_name(name)
        if pool:
            return pool.json(), 200
        return {'message': 'Item not found'}, 404

    def post(self, name):

        data = Pool.parser.parse_args()

        pool_id = PoolModel.find_by_id(data['pool_id'])
        if pool_id:
            return {"message": "this pool id already exists"}, 400
        pool_name = PoolModel.find_by_name(name)
        if pool_name:
            return {"message": "this pool name already exists"}, 400

        new_pool = PoolModel(data['pool_id'], name)
        try:
            new_pool.save_to_db()
        except:
            return {"message": "An error occurred inserting the new pool" }

        # for i in [0, data['pools_number']]:
        #     new_street = StreetModel(data['pool_id'])
        #     try:
        #         new_street.save_to_db()
        #     except:
        #         return {"message": "An error occurred inserting the streets" }

        return new_pool.json(), 201








class PoolList(Resource):
    def get(self):
        return {'pools': list(map(lambda x: x.json(), PoolModel.query.all()))}

        # return {'pools': [pool.json() for pool in PoolModel.query.all()]}, 200
        # pools = []
        # for center in centers:
        #     pools.append(center['name'])
        # return jsonify({'pools': pools})

