import unittest
from unittest.mock import MagicMock
from controllers.facebook_controller import FacebookController

class TestFacebookController(unittest.TestCase):

	@classmethod
	def setUp():
		self.facebook_facade = FacebookFacade()

	def should_call_posts_facade_for_posts_pile_saving(self):
		facebook_facade.get_all_posts_from_page = MagicMock()
		facebook_facade.get_page_posts = MagicMock()

		controller = FacebookController(facebook_facade)
		controller.save_all_posts_from_a_page_in_a_pile()

		facebook_facade.get_all_posts_from_page.assert_called()
		facebook_facade.get_page_posts.assert_called()

	def should_call_comments_facade_for_comment_saving(self):
		facebook_facade.get_page_posts = MagicMock()


if __name__ == '__main__':
	unittest.main()
