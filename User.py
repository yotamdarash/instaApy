from client import Instagram


class User(Instagram):
    def __init__(self, **kwargs):
        super(**kwargs)

    def self(self):
        pass

    def self_recent_media(self, count=None, min_id=None, max_id=None):
        pass

    def user_id(self, user_id):
        pass

    def user_recent_media(self, user_id, count=None, min_id=None, max_id=None):
        pass

    def self_liked(self, count=None, max_like_id=None):
        pass

    def search(self, query, count = None):
        pass
