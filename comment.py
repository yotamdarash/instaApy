from client import Client


class Comment(Client):
    endpoint_base = "/media"

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def get_comments(self, media_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(media_id) + "/comments"
        return self.get_request(endpoint, oauth_params, params)

    def post_comment(self, media_id, text):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {"text": text}
        endpoint = self.endpoint_base + "/" + str(media_id) + "/comments"
        return self.post_request(endpoint, oauth_params, params)

    def delete_comment(self, media_id, comment_id):
        oauth_params = self.ACCESS_TOKEN_ONLY
        params = {}
        endpoint = self.endpoint_base + "/" + str(media_id) + "/comments/" + str(comment_id)
        return self.delete_request(endpoint, oauth_params, params)
