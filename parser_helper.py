import json

def get_envelope(response):
    return json.loads(response.text)

def get_meta(response):
    return get_envelope(response)["meta"]

def get_data(response):
    return get_envelope(response)["data"]

