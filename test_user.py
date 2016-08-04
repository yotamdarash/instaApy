from unittest import TestCase

from user import User


class TestUser(TestCase):
    user = None

    def setUp(self):
        self.user = User(client_id='b3e2bf83b14747e89cb526adf934563c',
                         client_secret='7855bdc2ae4341468784204895aaa0a6',
                         client_ips='189464193',
                         access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                         redirect_uri=None)

    def test_user_self(self):
        response = self.user.self()
        self.assertEqual(response.code, 200)

    def test_user_self_recent_media_response_code(self):
        response = self.user.self_recent_media()
        self.assertEqual(response.code, 200)

    def test_user_self_recent_media_count(self):
        response = self.user.self_recent_media(count=2)
        self.assertEqual(len(response.body["data"]), 2)

    def test_user_id(self):
        response = self.user.user_id(189464193)
        self.assertEqual(response.code, 200)

    def test_self_liked(self):
        response = self.user.self_liked()
        self.assertEqual(response.code, 200)

    def test_search(self):
        response = self.user.search("meshu")
        self.assertEqual(response.code, 200)
