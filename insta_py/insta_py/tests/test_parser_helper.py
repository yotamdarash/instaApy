from unittest import TestCase

from app_info import AppInfo
from insta_py import InstagramAPI, get_meta, get_pagination, get_data, get_envelope


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