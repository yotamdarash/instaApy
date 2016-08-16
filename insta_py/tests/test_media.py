from unittest import TestCase

from app_info import AppInfo
from insta_py import InstagramAPI

class TestMedia(TestCase):
    media = None

    def setUp(self):
        instagramAPI = InstagramAPI(access_token=AppInfo.access_token)
        self.media = instagramAPI.media

    def test_media_id(self):
        response = self.media.media_id("1238562854941068266_189464193")
        self.assertEqual(response.status_code, 200)

    def test_media_shortcode(self):
        response = self.media.media_shortcode("BErotNxQYnK")
        self.assertEqual(response.status_code, 200)

    def test_media_search(self):
        response = self.media.search(latitude=48.858844, longitude=2.294351)
        self.assertEqual(response.status_code, 200)
