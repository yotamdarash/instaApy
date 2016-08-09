from unittest import TestCase
from instagramAPI import InstagramAPI
import parser_helper

class TestGet_envelope(TestCase):
    MEDIA_ID = "1238562854941068266_189464193"

    api = InstagramAPI(access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e')

    def setUp(self):
        pass
    def test_get_envelope(self):
        response = self.api.comments.get_comments(self.MEDIA_ID)
        envelope = parser_helper.get_envelope(response)
        self.assertTrue(all(key in envelope for key in ("meta", "data")))