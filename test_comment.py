from unittest import TestCase
from app_info import AppInfo
from comment import Comment


class TestComment(TestCase):
    comment = None
    #TODO: reset and hide access token
    def setUp(self):
        self.comment = Comment(access_token=AppInfo.access_token)
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
