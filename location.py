from client import Client


class Locations(Client):
    endpoint_base = "/locations"

    def __init__(self, **kwargs):
        super(Locations, self).__init__(**kwargs)

    def locations_info(self, location_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(location_id)
        return self.get_request(endpoint, oauth_params, params)

    def locations_recent_media(self, location_id, min_id=None, max_id=None):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}

        if min_id:
            params["min_id"] = min_id
        if max_id:
            params["max_id"] = max_id
        endpoint = self.endpoint_base + "/" + str(location_id)
        return self.get_request(endpoint, oauth_params, params)

    def locations_search(self, latitude=None, longitude=None, distance=500, facebook_places_id=None):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        if latitude and longitude:
            params.update({"lat": latitude, "lng": longitude})
        if distance != 500:
            params["distance"] = distance
        if facebook_places_id:
            params["facebook_places_id"] = facebook_places_id
        endpoint = self.endpoint_base + "/search"
        return self.get_request(endpoint, oauth_params, params)
