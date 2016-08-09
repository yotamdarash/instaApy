import json

def get_envelope(response):
    response_in_json = json.loads(response.text)
    return response_in_json


def get_meta(response):
    meta = get_envelope(response)["meta"]
    return meta
