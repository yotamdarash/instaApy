from unittest import TestCase

import parser_helper
from instagramAPI import InstagramAPI


class TestGet_envelope(TestCase):
    MEDIA_ID = "1238562854941068266_189464193"
    api = InstagramAPI(access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e')
    test_response = None

    def setUp(self):
        self.test_response = self.api.comments.get_comments(self.MEDIA_ID)

    def test_get_envelope(self):
        envelope = parser_helper.get_envelope(self.test_response)
        self.assertTrue(all(key in envelope for key in ("meta", "data")))

    def test_get_meta(self):
        meta = parser_helper.get_meta(self.test_response)
        self.assertTrue("code" in meta)

    def test_get_data(self):
        data = parser_helper.get_data(self.test_response)
        self.assertIsNotNone(data)
