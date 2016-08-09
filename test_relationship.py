from unittest import TestCase

from relationship import Relationship


class TestRelationship(TestCase):
    relationship = None

    def setUp(self):
        self.relationship = Relationship(client_id='b3e2bf83b14747e89cb526adf934563c',
                                         client_secret='7855bdc2ae4341468784204895aaa0a6',
                                         client_ips='189464193',
                                         access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                                         redirect_uri=None)
        self.user_id_to_test = "189464193"

    def test_follows(self):
        response = self.relationship.follows()
        self.assertEqual(response.status_code, 200)

    def test_followed_by(self):
        response = self.relationship.followed_by()
        self.assertEqual(response.status_code, 200)

    def test_requested_by(self):
        response = self.relationship.requested_by()
        self.assertEqual(response.status_code, 200)

    def test_get_relationship(self):
        response = self.relationship.get_relationship(self.user_id_to_test)
        self.assertEqual(response.status_code, 200)

    def test_modify_relationship(self):
        response = self.relationship.modify_relationship(self.user_id_to_test, "unfollow")
        self.assertEqual(response.status_code, 200)
