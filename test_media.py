from unittest import TestCase

from app_info import AppInfo
from media import Media


class TestMedia(TestCase):
    media = None

    def setUp(self):
        self.media = Media(access_token=AppInfo.access_token)

    def test_media_id(self):
        response = self.media.media_id("1238562854941068266_189464193")
        self.assertEqual(response.status_code, 200)

    def test_media_shortcode(self):
        response = self.media.media_shortcode("BErotNxQYnK")
        self.assertEqual(response.status_code, 200)

    def test_media_search(self):
        response = self.media.search(latitude=48.858844, longitude=2.294351)
        self.assertEqual(response.status_code, 200)
