import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from modules.facebook_facade import FacebookFacade

class TestFacebookFacade(unittest.TestCase):

	def test_should_call_get_page_posts_on_getting_page(self):
		facebook_facade = FacebookFacade()

		facebook_facade.get_page_posts = MagicMock()
		facebook_facade.get_page_posts.return_value = "{}"
		facebook_facade.posts_facade.iterate_and_save_posts = MagicMock()

		facebook_facade.get_all_posts_from_page("some valid id", "some valid alias")

		facebook_facade.get_page_posts.assert_called()
		facebook_facade.posts_facade.iterate_and_save_posts.assert_called()

	def test_should_call_graphs_on_getting_page_posts(self):
		facebook_facade = FacebookFacade()
		facebook_facade.graph.get_object = MagicMock()
		facebook_facade.graph.get_connections = MagicMock()

		facebook_facade.get_page_posts("some page id")
		
		facebook_facade.graph.get_object.assert_called()
		facebook_facade.graph.get_connections.assert_called()

	def test_should_call_comments_facade_on_getting_comments_from_pile(self):
		facebook_facade = FacebookFacade()
		facebook_facade.comments_facade = MagicMock()
		facebook_facade.get_all_comments_from_posts_pile()
		
		facebook_facade.comments_facade.iterate_and_save_comments_from_pile.assert_called()

if __name__ == '__main__':
	unittest.main()