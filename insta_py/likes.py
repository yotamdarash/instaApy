import posixpath

from client import Client


class Likes(Client):
    endpoint_base = "/media"

    def __init__(self, **kwargs):
        super(Likes, self).__init__(**kwargs)

    def get_likes(self, media_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = posixpath.join(self.endpoint_base, str(media_id), "likes")
        return self._get_request(endpoint, oauth_params, params)

    def post_like(self, media_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint =posixpath.join(self.endpoint_base, str(media_id), "likes")
        return self._get_request(endpoint, oauth_params, params)

    def delete_like(self, media_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = posixpath.join(self.endpoint_base, str(media_id), "likes")
        return self._get_request(endpoint, oauth_params, params)
