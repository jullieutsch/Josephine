import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from modules.facebook_facade import FacebookFacade

class TestFacebookFacade(unittest.TestCase):

	@classmethod
	def setUp(self):
		original_input = __builtins__.input
		__builtins__.input = lambda _: "some_input_value"

		self.facebook_facade = FacebookFacade()

	def test_should_call_get_page_posts_on_getting_page(self):
		self.facebook_facade.get_page_posts = MagicMock()
		self.facebook_facade.get_page_posts.return_value = "{}"
		self.facebook_facade.posts_facade.iterate_and_save_posts = MagicMock()

		self.facebook_facade.get_all_posts_from_page("some valid id", "some valid alias")

		self.facebook_facade.get_page_posts.assert_called()
		self.facebook_facade.posts_facade.iterate_and_save_posts.assert_called()

	def test_should_call_graphs_on_getting_page_posts(self):
		self.facebook_facade.graph.get_object = MagicMock()
		self.facebook_facade.graph.get_connections = MagicMock()

		self.facebook_facade.get_page_posts("some page id")
		
		self.facebook_facade.graph.get_object.assert_called()
		self.facebook_facade.graph.get_connections.assert_called()

	def test_should_call_comments_facade_on_getting_comments_from_pile(self):
		self.facebook_facade.comments_facade.iterate_and_save_comments_from_pile = MagicMock()
		self.facebook_facade.get_all_comments_from_posts_pile("page alias")

		self.facebook_facade.comments_facade.iterate_and_save_comments_from_pile.assert_called()

if __name__ == '__main__':
	unittest.main()