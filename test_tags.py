from unittest import TestCase

from tags import Tags


class TestTags(TestCase):
    tags = None

    def setUp(self):
        self.tags = Tags(client_id='b3e2bf83b14747e89cb526adf934563c',
                         client_secret='7855bdc2ae4341468784204895aaa0a6',
                         client_ips='189464193',
                         access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                         redirect_uri=None)
        self.tag_to_search = "paleo"

    def test_tags_info(self):
        response = self.tags.tags_info(self.tag_to_search)
        self.assertEqual(response.status_code, 200)

    def test_tags_rcent_media(self):
        response = self.tags.tags_recent_media(self.tag_to_search)
        self.assertEqual(response.status_code, 200)

    def test_tags_search(self):
        response = self.tags.tags_info(self.tag_to_search)
        self.assertEqual(response.status_code, 200)
