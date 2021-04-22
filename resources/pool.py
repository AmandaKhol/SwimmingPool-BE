
from flask import Flask, jsonify
from flask_restful import Resource
from centers import centers


class PoolList(Resource):
    def get(self):
        pools = []
        for center in centers:
            pool = {'name': center['name']}
            pools.append(pool)
        return jsonify({'pools': pools})
