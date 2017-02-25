from geo_tracker import db

class GeoLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, user_id, lat, lng):
        self.user_id = user_id
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<GeoLocation %r %r %r>' % (self.user_id, self.lat, self.lng)

