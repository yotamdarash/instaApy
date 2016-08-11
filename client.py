import requests

from oauth2 import OAuth2API


class Client(OAuth2API):
    host = "https://api.instagram.com"
    base_path = "/v1"
    header_default = {"Accept": "application/json"}
    ACCESS_TOKEN_ONLY = ["access_token"]


    def __init__(self, **kwargs):
        super(Client, self).__init__(**kwargs)

    def _build_path(self, endpoint): #TODO: make private
        return self.host + self.base_path + endpoint

    def _build_params(self, params):
        return params

    def _build_oauth_params(self, params):
        if params == self.ACCESS_TOKEN_ONLY:
            return {"access_token": self.access_token}
        else:
            raise NotImplementedError("ouath params {} not implemented".format(params))

    def _parse_request(self, endpoint, accepted_oauth_params, accepted_params):
        path = self._build_path(endpoint)
        params = self._build_params(accepted_params)
        params.update(self._build_oauth_params(accepted_oauth_params))

        return path, params

    def _get_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self._parse_request(endpoint, accepted_oauth_params, accepted_params)
        r = requests.get(path, params=params)
        return r

    def _post_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self._parse_request(endpoint, accepted_oauth_params, accepted_params)
        r = requests.post(path, data=params)
        return r

    def _delete_request(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self._parse_request(endpoint, accepted_oauth_params, accepted_params)
        r = requests.delete(path, params=params)
        return r
