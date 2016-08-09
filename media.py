from client import Client


class Media(Client):
    endpoint_base = "/media"

    def __init__(self, **kwargs):
        super(Media, self).__init__(**kwargs)

    def media_id(self, media_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(media_id)
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def media_shortcode(self, shortcode):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/shortcode/" + str(shortcode)
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def media_search(self, latitude=None, longitude=None, distance=1000):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        if latitude and longitude:
            params.update({"lat": latitude, "lng": longitude})
        if distance != 1000:
            params["distance"] = distance
        endpoint = self.endpoint_base + "/search"
        response = self.get_request(endpoint, oauth_params, params)
        return response
