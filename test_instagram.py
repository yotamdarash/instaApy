from unittest import TestCase

from client import Instagram
from User import User

class TestInstagram(TestCase):
    def setUp(self):
        api = Instagram(client_id='b3e2bf83b14747e89cb526adf934563c',
                        client_secret='7855bdc2ae4341468784204895aaa0a6',
                        client_ips='189464193',
                        access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                        redirect_uri=None)

    def setup_user(self):
        user =

    def test_user_self(self):
        self.fail()

    def test_user_self_recent_media(self):
        self.fail()

    def test_user_id(self):
        self.fail()

    def test_self_liked(self):
        self.fail()

    def test_search(self):
        self.fail()
