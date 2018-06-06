import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import modules.comment_analysis

class TestCommentAnalysis(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		self.comment_analysis = modules.comment_analysis
		
	def test_get_comments_occurrence(self):
		self.fake_db_definition_with_two_records()
		self.comment_analysis.get_comment_date = MagicMock()

		self.comment_analysis.get_comments_occurrence(self.db_mock, "some_alias")
		
		self.db_mock.keys.assert_called()
		self.assertEqual(self.db_mock.hmget.call_count, 2)
		self.assertEqual(self.comment_analysis.get_comment_date.call_count, 2)

	def test_get_comment_date(self):
		date = self.comment_analysis.get_comment_date(
			self.generate_comment_created_datetime())
		self.assertEqual(str(date), "2017-01-07")

	def fake_db_definition_with_two_records(self):
		self.db_mock = MagicMock()
		self.db_mock.keys = Mock(return_value = ["first_key", "second_key"])
		self.db_mock.hmget = MagicMock()


	def generate_comment_created_datetime(self):
		return '2017-01-07T23:27:04+0000'

	"""def face_db_ocurrences_generator():
		return "{[
			{
				"message": "this is the first occurrence!"
			},
			{
				"message": "this is the second occurrence!"
			}	
		
		]}"""
if __name__ == '__main__':
	unittest.main()
