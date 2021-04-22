from db import db

class PoolModel(db.Model):
    __tablename__ = 'pools'

    id = db.Column(db.Integer, primary_key=True)
    pool_name = db.Column(db.String(20))

    #Back reference
    streets = db.relationship('StreetModel', lazy='dynamic')

    def __init__(self, pool_name):
        self.pool_name = pool_name

    def json(self):
        return {
                'pool_name': self.pool_name,
                'streets': [street.json() for street in self.streets.all()]
        }

    @classmethod
    def find_by_id(cls, pool_id):
        return cls.query.filter_by(id=pool_id).first();