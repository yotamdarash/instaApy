from unittest import TestCase
from app_info import AppInfo
from tags import Tags


class TestTags(TestCase):
    tags = None

    def setUp(self):
        self.tags = Tags(access_token=AppInfo.access_token)
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
