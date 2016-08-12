from unittest import TestCase

from insta_py import InstagramAPI

from app_info import AppInfo


class TestTags(TestCase):
    tags = None

    def setUp(self):
        instagramAPI = InstagramAPI(access_token=AppInfo.access_token)
        self.tags = instagramAPI.tags
        self.tag_to_search = "paleo"

    def test_tags_info(self):
        response = self.tags.tag_info(self.tag_to_search)
        self.assertEqual(response.status_code, 200)

    def test_tags_rcent_media(self):
        response = self.tags.tag_recent_media(self.tag_to_search)
        self.assertEqual(response.status_code, 200)

    def test_tags_search(self):
        response = self.tags.search(self.tag_to_search)
        self.assertEqual(response.status_code, 200)
