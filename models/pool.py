from db import db

class PoolModel(db.Model):
    __tablename__ = 'pools'

    id = db.Column(db.Integer, primary_key=True)
    pool_name = db.Column(db.String(20))

    #Back reference
    streets = db.relationship('StreetModel', lazy='dynamic')

    def __init__(self, pool_id, pool_name):
        self.id = pool_id
        self.pool_name = pool_name.lower()

    def json(self):
        return {
                'id': self.id,
                'pool_name': self.pool_name,
                'streets': [street.json() for street in self.streets.all()]
        }

    @classmethod
    def find_by_id(cls, pool_id):
        return cls.query.filter_by(id=pool_id.lower()).first()

    @classmethod
    def find_by_name(cls, pool_name):
        return cls.query.filter_by(pool_name=pool_name.lower()).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()