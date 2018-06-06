import unittest
from unittest.mock import MagicMock
from modules.models.facebook_comment import FacebookComment

class TestFacebookComment(unittest.TestCase):

	def test_should_key_error_on_invalid_field(self):
		db = MagicMock()
		comment_data = {'message': 'hello, world', 'id': '123', 'created_time': '12345'}
		facebook_comment = FacebookComment()
		facebook_comment.save(db, "page_alias", comment_data)
		db.hmset.assert_called_with("comments:page_alias:saved:123", comment_data)

	def test_should_save_on_redis_with_proper_object(self):
		db = MagicMock()
		incomplete_comment_data = {'message': 'hello, world', 'id': '123'}
		facebook_comment = FacebookComment()
		self.assertRaises(KeyError, lambda: facebook_comment.save(db, "page_alias", incomplete_comment_data))

if __name__ == '__main__':
	unittest.main()

