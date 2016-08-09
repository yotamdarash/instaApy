from client import Client


class Tags(Client):
    endpoint_base = "/tags"

    def __init__(self, **kwargs):
        super(Tags, self).__init__(**kwargs)

    def tags_info(self, tag_name):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(tag_name)
        return self.get_request(endpoint, oauth_params, params)

    def tags_recent_media(self, tag_name, count=None, min_tag_id=None, max_tag_id=None):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        if count:
            params["count"] = count
        if min_tag_id:
            params["mind_tag_id"] = min_tag_id
        if max_tag_id:
            params["max_tag_id"] = max_tag_id
        endpoint = self.endpoint_base + "/" + str(tag_name)
        return self.get_request(endpoint, oauth_params, params)

    def tags_search(self, query):
        oauth_params = self.ACCESS_TOKEN_ONLY
        if query[0] == "#":
            raise ValueError("Query string must be without a leading #")
        params = {"q": query}
        endpoint = self.endpoint_base + "/search"
        response = self.get_request(endpoint, oauth_params, params)
        return response
