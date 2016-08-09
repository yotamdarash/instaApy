from comment import Comment
from likes import Likes
from location import Locations
from media import Media
from relationship import Relationship
from tags import Tags
from user import User


class InstagramAPI():
    def __init__(self, access_token, client_id=None,
                 client_secret=None,
                 client_ips=None,
                 redirect_uri=None):
        self.users = User(access_token=access_token)
        self.relationships = Relationship(access_token=access_token)
        self.media = Media(access_token=access_token)
        self.comments = Comment(access_token=access_token)
        self.likes = Likes(access_token=access_token)
        self.tags = Tags(access_token=access_token)
        self.locations = Locations(access_token=access_token)
    