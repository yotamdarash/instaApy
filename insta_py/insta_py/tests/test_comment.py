from unittest import TestCase
from app_info import AppInfo
from insta_py import InstagramAPI

class TestComment(TestCase):
    comment = None

    def setUp(self):
        instagramAPI = InstagramAPI(access_token=AppInfo.access_token)
        self.comment = instagramAPI.comments
        self.media_id_to_test = "1238562854941068266_189464193"

    def test_get_comments(self):
        response = self.comment.get_comments(self.media_id_to_test)
        self.assertEqual(response.status_code, 200)

    def test_post_comment(self):
        response = self.comment.post_comment(self.media_id_to_test,
                                             "commentfrompythonwrapper")
        self.assertEqual(response.status_code, 200)

    def test_delete_comment(self):
        response = self.comment.delete_comment(self.media_id_to_test, "17859821500037944")
        self.assertEqual(response.status_code, 200)
