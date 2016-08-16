import json

import models


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


def _build_pagination_info(content_obj):
    """Extract pagination information in the desired format."""
    pagination = content_obj.get('pagination', {})
    # if self.pagination_format == 'next_url':
    #     return pagination.get('next_url')
    # if self.pagination_format == 'dict':
    return pagination
    # raise Exception('Invalid value for pagination_format: %s' % self.pagination_format)


def parse_media(response):
    return models.Media(get_data(response)), _build_pagination_info(get_envelope(response))


def parse_user(response):
    return models.User(get_data(response)), _build_pagination_info(get_envelope(response))


def parse_tag(response):
    return models.Tag(get_data(response)), _build_pagination_info(get_envelope(response))


def parse_comment(response):
    api_response = []
    for entry in get_data(response):
        obj = models.Tag(entry)
        api_response.append(obj)
    return api_response, _build_pagination_info(get_envelope(response))


def parse_relationship(response):
    return models.Relationship(get_data(response)), _build_pagination_info(get_envelope(response))


def parse_shortcode(response):
    return models.MediaShortcode(**get_data(response)), _build_pagination_info(get_envelope(response))


def parse_location(response):
    return models.Location(**dict(get_data(response))), _build_pagination_info(get_envelope(response))
