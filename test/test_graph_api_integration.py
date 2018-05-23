import unittest
from modules.facebook_facade import FacebookFacade
import facebook

class TestGraphAPIIntegration(unittest.TestCase):

	def test_should_prompt_for_valid_key_when_none_is_given(self):
		original_input = __builtins__.input
		__builtins__.input = lambda _: "some invalid key"
		facebook_facade = FacebookFacade()
		self.assertRaises(ValueError, 
		lambda: facebook_facade.get_all_posts_from_page("some page id", "some page alias"))

if __name__ == '__main__':
	unittest.main()
