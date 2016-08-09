from unittest import TestCase

from likes import Likes


class TestLikes(TestCase):
    likes = None

    def setUp(self):
        self.likes = Likes(client_id='b3e2bf83b14747e89cb526adf934563c',
                           client_secret='7855bdc2ae4341468784204895aaa0a6',
                           client_ips='189464193',
                           access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                           redirect_uri=None)
        self.media_id_to_test = "1238562854941068266_189464193"

    def test_get_liked(self):
        response = self.likes.get_likes(self.media_id_to_test)
        self.assertEqual(response.status_code, 200)

    def test_post_like(self):
        response = self.likes.post_like(self.media_id_to_test)
        self.assertEqual(response.status_code, 200)

    def test_delete_like(self):
        response = self.likes.delete_like(self.media_id_to_test)
        self.assertEqual(response.status_code, 200)
