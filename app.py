from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from resources.hour import HourList
from resources.pool import PoolList

app = Flask(__name__)
CORS(app=app)
api = Api(app)

api.add_resource(PoolList, '/')
api.add_resource(HourList, '/<string:poolId>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)