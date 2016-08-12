from unittest import TestCase

from app_info import AppInfo
from insta_py import InstagramAPI

class TestRelationship(TestCase):
    relationship = None

    def setUp(self):
        instagramAPI = InstagramAPI(access_token=AppInfo.access_token)
        self.relationship = instagramAPI.relationships
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
