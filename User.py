from client import Instagram


class User(Instagram):
    endpoint_base = "/users"

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def self(self):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/self"
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def self_recent_media(self, count=None, min_id=None, max_id=None):
        pass

    def user_id(self, user_id):
        pass

    def user_recent_media(self, user_id, count=None, min_id=None, max_id=None):
        pass

    def self_liked(self, count=None, max_like_id=None):
        pass

    def search(self, query, count=None):
        pass
