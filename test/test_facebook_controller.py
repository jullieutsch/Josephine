import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from controllers.facebook_controller import FacebookController
from modules.facebook_facade import FacebookFacade
import modules.comment_analysis

class TestFacebookController(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.facebook_facade = FacebookFacade()
		self.comment_analysis = modules.comment_analysis
		self.controller = FacebookController(self.facebook_facade, 
			self.comment_analysis)


	def test_should_call_posts_facade_for_posts_pile_saving(self):
		self.facebook_facade.get_all_posts_from_page = MagicMock()
		self.controller.save_all_posts_from_a_page_in_a_pile()

		self.facebook_facade.get_all_posts_from_page.assert_called()

	def test_should_call_comments_facade_for_comment_saving(self):
		self.facebook_facade.get_all_comments_from_posts_pile = MagicMock()	
		self.controller.saves_all_comments_from_unsaved_posts_pile()

		self.facebook_facade.get_all_comments_from_posts_pile.assert_called()

	def test_generate_csv_for_comment_ocurrence_on_corpus(self):
		self.comment_analysis.get_comments_occurrence = Mock()

		self.controller.generate_csv_for_comment_ocurrence_on_corpus(self.facebook_facade.db)
		self.comment_analysis.get_comments_occurrence.assert_called()

if __name__ == '__main__':
	unittest.main()
