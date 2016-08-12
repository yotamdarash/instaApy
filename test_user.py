import json
from unittest import TestCase

from app_info import AppInfo
from user import User


class TestUser(TestCase):
    user = None

    def setUp(self):
        self.user = User(access_token=AppInfo.access_token)

    def test_user_self(self):
        response = self.user.self()
        self.assertEqual(response.status_code, 200)

    def test_user_self_recent_media_response_code(self):
        response = self.user.self_recent_media()
        self.assertEqual(response.status_code, 200)

    def test_user_self_recent_media_count(self):
        response = self.user.self_recent_media(count=2)
        parsed_response = json.loads(response.text)
        self.assertEqual(len(parsed_response["data"]), 2)

    def test_user_id(self):
        response = self.user.user_id(189464193)
        self.assertEqual(response.status_code, 200)

    def test_self_liked(self):
        response = self.user.self_liked()
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.user.search("meshu")
        self.assertEqual(response.status_code, 200)
