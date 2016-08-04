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
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        if count:
            params.update({"count": count})
        if min_id:
            params.update({"mind_id": min_id})
        if max_id:
            params.update({"max_id": max_id})
        endpoint = self.endpoint_base + "/self/media/recent"
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def user_id(self, user_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(user_id)
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def user_recent_media(self, user_id, count=None, min_id=None, max_id=None):
        pass

    def self_liked(self, count=None, max_like_id=None):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        if count:
            params.update({"count": count})
        if max_like_id:
            params.update({"max_like_id": max_like_id})
        endpoint = self.endpoint_base + "/self/media/liked"
        response = self.get_request(endpoint, oauth_params, params)
        return response

    def search(self, query, count=None):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {"q": query}
        if count:
            params.update({"count": count})
        endpoint = self.endpoint_base + "/search"
        response = self.get_request(endpoint, oauth_params, params)
        return response
