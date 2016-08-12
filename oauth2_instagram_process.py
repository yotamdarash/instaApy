import json

import requests


def generate_authorization_url(client_id, redirect_url, scope=None):
    url = "https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code".format(client_id,
                                                                                                              redirect_url)
    if scope:
        if isinstance(scope, basestring):
            url += "&scope=" + scope
        else:
            url += "&scope=" + "+".join(scope)
    return url


def get_authorization_token(code,
                            client_id,
                            client_secret,
                            redirect_url,
                            grant_type="authorization_code"):
    params = {"client_id": client_id,
              "client_secret": client_secret,
              "redirect_uri": redirect_url,
              "grant_type": grant_type,
              "code": code
              }
    r = requests.post("https://api.instagram.com/oauth/access_token", data=params)
    return json.loads(r.text)
