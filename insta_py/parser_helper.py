import json


def get_envelope(response):
    return json.loads(response.text)


def get_meta(response):
    return get_envelope(response)["meta"]


def get_data(response):
    return get_envelope(response)["data"]


def get_pagination(response):
    parsed_response = get_envelope(response)
    if "pagination" in parsed_response:
        return parsed_response["pagination"]
    else:
        return None
