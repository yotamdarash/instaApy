class OAuth2API(object):
    host = None
    base_path = None
    authorize_url = None
    access_token_url = None
    redirect_uri = None
    # some providers use "oauth_token"
    access_token_field = "access_token"
    protocol = "https"
    api_name = "Generic API"

    def __init__(self, client_id=None, client_secret=None, client_ips=None, access_token=None, redirect_uri=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_ips = client_ips
        self.access_token = access_token
        self.redirect_uri = redirect_uri
