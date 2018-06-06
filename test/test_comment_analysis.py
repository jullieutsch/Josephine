import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import modules.comment_analysis

class TestCommentAnalysis(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		self.comment_analysis = modules.comment_analysis
		
	def test_get_comments_occurrence(self):
		self.fake_db_definition()

		self.comment_analysis.get_comments_occurrence(self.db_mock, "some_alias")
		self.comment_analysis.get_comment_date = MagicMock()
		
		self.db_mock.keys.assert_called()
		self.assertEqual(self.db_mock.get.call_count, 2)

	def fake_db_definition(self):
		self.db_mock = MagicMock()
		self.db_mock.keys = Mock(return_value = ["first_key", "second_key"])
		self.db_mock.get = MagicMock()

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
