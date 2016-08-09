from unittest import TestCase

from media import Media


class TestMedia(TestCase):
    media = None

    def setUp(self):
        self.media = Media(client_id='b3e2bf83b14747e89cb526adf934563c',
                           client_secret='7855bdc2ae4341468784204895aaa0a6',
                           client_ips='189464193',
                           access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                           redirect_uri=None)

    def test_media_id(self):
        response = self.media.media_id("1238562854941068266_189464193")
        self.assertEqual(response.status_code, 200)

    def test_media_shortcode(self):
        response = self.media.media_shortcode("BErotNxQYnK")
        self.assertEqual(response.status_code, 200)

    def test_media_search(self):
        response = self.media.media_search(latitude=48.858844, longitude=2.294351)
        self.assertEqual(response.status_code, 200)
