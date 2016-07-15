import unirest

from oauth2 import OAuth2API


class Instagram(OAuth2API):
    host = "api.instagram.com"
    base_path = "/v1"
    header_default = {"Accept": "application/json"}

    def __init__(self, **kwargs):
        super(**kwargs)

    def build_path(self, endpoint):
        return self.host + self.base_path + endpoint

    def build_params(self, params):
        return params

    def parse_request(self, endpoint, accepted_oauth_params, accepted_params):
        path = self.build_path(endpoint)
        params = self.build_param(accepted_params)
        params.update(self.build_param(accepted_oauth_params))

        return path, params

    def get_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self.parse_request(endpoint, accepted_oauth_params, accepted_params)
        return unirest.get(path, headers=self.header_default, params=params)
