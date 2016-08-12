from unittest import TestCase

from app_info import AppInfo
from likes import Likes


class TestLikes(TestCase):
    likes = None

    def setUp(self):
        self.likes = Likes(access_token=AppInfo.access_token)
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
