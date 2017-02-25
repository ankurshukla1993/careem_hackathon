from geo_tracker import api
from geo_tracker.models.geo_locations import GeoLocation 
class RGeoLocation(Resource):
    def get(self, geo_location_id):
        return {'hello': 'world'}

api.add_resource(RGeoLocation, '/<integer:geo_location_id>')

