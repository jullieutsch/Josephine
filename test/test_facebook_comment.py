import unittest
from unittest.mock import MagicMock
from modules.models.facebook_comment import FacebookComment

class TestFacebookComment(unittest.TestCase):

	def test_should_key_error_on_invalid_field(self):
		db = MagicMock()
		comment_data = {'message': 'hello, world', 'id': '123', 'created_time': '12345'}
		facebook_comment = FacebookComment(db, comment_data)
		assert facebook_comment.comment_map["message"] == "hello, world"

	def test_should_save_on_redis_with_proper_object(self):
		db = MagicMock()
		incomplete_comment_data = {'message': 'hello, world', 'id': '123'}
		self.assertRaises(KeyError, lambda: FacebookComment(db, incomplete_comment_data))

if __name__ == '__main__':
	unittest.main()

