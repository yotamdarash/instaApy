from unittest import TestCase

from app_info import AppInfo
from insta_py import InstagramAPI, get_meta, get_pagination, get_data, get_envelope, \
    parse_media, parse_user, parse_tag, parse_comment, parse_relationship, parse_location


class TestGet_envelope(TestCase):
    MEDIA_ID = "1238562854941068266_189464193"
    api = InstagramAPI(access_token=AppInfo.access_token)
    test_response = None

    def setUp(self):
        self.test_response = self.api.users.self_recent_media()

    def test_get_envelope(self):
        envelope = get_envelope(self.test_response)
        self.assertTrue(all(key in envelope for key in ("meta", "data")))

    def test_get_meta(self):
        meta = get_meta(self.test_response)
        self.assertTrue("code" in meta)

    def test_get_data(self):
        data = get_data(self.test_response)
        self.assertIsNotNone(data)

    def test_get_pagination(self):
        pagination = get_pagination(self.test_response)
        self.assertIsNotNone(pagination)

    def test_parse_media(self):
        response = self.api.users.self_recent_media(count=2)
        media, pagination = parse_media(response)
        try:
            self.assertIsNotNone(media.id)
        except TypeError:
            self.fail()

    def test_parse_user(self):
        response = self.api.users.self()
        user, pagination = parse_user(response)
        try:
            self.assertIsNotNone(user.id.username)
        except TypeError:
            self.fail()

    def test_parse_tag(self):
        response = self.api.tags.tag_info("paleo")
        tag, pagination = parse_tag(response)
        try:
            self.assertIsNotNone(tag.name.media_count)
        except TypeError:
            self.fail()

    def test_parse_comment(self):
        response = self.api.comments.get_comments(self.MEDIA_ID)
        comment, pagination = parse_comment(response)
        try:
            self.assertIsNotNone(comment[0].name)
        except TypeError:
            self.fail()

    def test_parse_relationship(self):
        response = self.api.relationships.follows()
        relationship, pagination = parse_relationship(response)
        try:
            self.assertIsNotNone(relationship.incoming_status)
        except TypeError:
            self.fail()

    def test_parse_location(self):
        response = self.api.locations.locations_info(1)
        location, pagination = parse_location(response)
        try:
            self.assertIsNotNone(location.incoming_status)
        except TypeError:
            self.fail()
