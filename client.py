import unirest
from oauth2 import OAuth2API


class Client(OAuth2API):
    host = "http://api.instagram.com"
    base_path = "/v1"
    header_default = {"Accept": "application/json"}
    ACCESS_TOKEN_ONLY = ["access_token"]

    def __init__(self, **kwargs):
        super(Client, self).__init__(**kwargs)

    def build_path(self, endpoint):
        return self.host + self.base_path + endpoint

    def build_params(self, params):
        return params

    def build_oauth_params(self, params):
        if params == self.ACCESS_TOKEN_ONLY:
            return {"access_token": self.access_token}
        else:
            raise NotImplementedError("ouath params {} not implemented".format(params))

    def parse_request(self, endpoint, accepted_oauth_params, accepted_params):
        path = self.build_path(endpoint)
        params = self.build_params(accepted_params)
        params.update(self.build_oauth_params(accepted_oauth_params))

        return path, params

    def get_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self.parse_request(endpoint, accepted_oauth_params, accepted_params)
        return unirest.get(path, headers=self.header_default, params=params)

    def post_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self.parse_request(endpoint, accepted_oauth_params, accepted_params)
        return unirest.post(path, headers=self.header_default, params=params)

    def delete_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self.parse_request(endpoint, accepted_oauth_params, accepted_params)
        return unirest.delete(path, headers=self.header_default, params=params)