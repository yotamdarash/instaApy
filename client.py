import unirest

from oauth2 import OAuth2API


class Instagram(OAuth2API):
    host = "api.instagram.com"
    base_path = "/v1"
    header_default = {"Accept": "application/json"}

    def __init__(self, **kwargs):
        super(**kwargs)

    def buildPath(self, endpoint):
        return self.host + self.base_path + endpoint

    def buildParams(self, params):
        return params

    def parseRequest(self, endpoint, accepted_oauth_params, accepted_params):
        path = self.buildPath(endpoint)
        params = self.buildParam(accepted_params)
        params.update(self.buildParam(accepted_oauth_params))

        return path, params

    def getRequest(self, endpoint, accepted_oauth_params, accepted_params):
        path, params = self.parseRequest(endpoint, accepted_oauth_params, accepted_params)
        return unirest.get(path, headers=self.header_default, params=params)
