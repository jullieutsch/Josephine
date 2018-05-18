import unittest
from source.modules.facebook_facade import FacebookFacade

class TestFacebookFacade(unittest.TestCase):
			
	def test_should_prompt_for_valid_key_when_none_is_given(self):
		facebook_facade = FacebookFacade("some invalid key")
		self.assertRaises(ValueError, 
			lambda: facebook_facade.get_all_posts_from_page("some page"))

if __name__ == '__main__':
	unittest.main()
