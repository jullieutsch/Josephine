import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import modules.comment_analysis

class TestCommentAnalysis(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		self.comment_analysis = modules.comment_analysis
		
	def test_get_comments_occurrence_with_two_records_retrieves_correct_count(self):
		self.fake_db_definition_with_two_records()
		self.comment_analysis.get_comment_date = MagicMock()

		occurrences = self.comment_analysis.get_comments_occurrence(self.db_mock, "some_alias")
		
		self.db_mock.keys.assert_called()
		self.assertEqual(self.db_mock.hmget.call_count, 2)
		self.assertEqual(self.comment_analysis.get_comment_date.call_count, 2)

	def test_get_comment_date(self):
		comment_date = self.comment_analysis.get_comment_date(
		self.generate_comment_created_datetime())

		self.assertEqual("2017-01-07", comment_date)

	def test_increment_comment_date(self):
		ocurrencies = self.comment_analysis.increment_date( "2017-01-07", {})
		ocurrencies = self.comment_analysis.increment_date("2017-01-07", ocurrencies)

		self.assertEqual(len(ocurrencies), 1)
		self.assertEqual(ocurrencies["2017-01-07"], 2)

	def fake_db_definition_with_two_records(self):
		self.db_mock = MagicMock()
		self.db_mock.keys = Mock(return_value = ["first_key", "second_key"])
		self.db_mock.hmget = MagicMock()


	def generate_comment_created_datetime(self):
		return '2017-01-07T23:27:04+0000'
if __name__ == '__main__':
	unittest.main()
