from facebook_facade import FacebookFacade
from comments_facade import FacebookCommentsFacade

class FacebookController:
	
	def __init__(self):
		print("Welcome to FacebookRedis Data Gathering")
		self.facebook_facade = FacebookFacade()

	def save_all_posts_from_a_page_in_a_pile(self):
		page_id = input("Please, enter page id")
		page_alias = input("Please, insert page alias for database")
		facebook_facade.get_all_posts_from_page(page_id, page_alias)
		#comments_facade.get_all_comments_from_posts_pile(page_id)
