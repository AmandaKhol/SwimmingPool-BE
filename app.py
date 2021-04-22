from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from resources.hour import HourList
from resources.pool import Pool, PoolList

app = Flask(__name__)
CORS(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(PoolList, '/')
api.add_resource(Pool, '/<string:pool_id>')
#api.add_resource(HourList, '/')
# api.add_resource(HourList, '/<string:poolId>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)