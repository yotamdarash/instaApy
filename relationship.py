from client import Client


class Relationship(Client):
    endpoint_base = "/users"
    ALLOWED_RELATIONSHIPS = ['follow', 'unfollow', 'approve', 'ignore']

    def __init__(self, **kwargs):
        super(Relationship, self).__init__(**kwargs)

    def follows(self):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/self/follows"
        return self.get_request(endpoint, oauth_params, params)

    def followed_by(self):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/self/followed-by"
        return self.get_request(endpoint, oauth_params, params)

    def requested_by(self):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/self/requested-by"
        return self.get_request(endpoint, oauth_params, params)

    def get_relationship(self, user_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(user_id) + "/relationship"
        return self.get_request(endpoint, oauth_params, params)

    def modify_relationship(self, user_id, action):
        oauth_params = self.ACCESS_TOKEN_ONLY
        if action not in self.ALLOWED_RELATIONSHIPS:
            raise ValueError("action must be of the following {} ".format(self.ALLOWED_RELATIONSHIPS))
        params = {"action": action}
        endpoint = self.endpoint_base + "/" + str(user_id) + "/relationship"
        return self.post_request(endpoint, oauth_params, params)
