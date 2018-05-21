from modules.facebook_facade import FacebookFacade

class FacebookController:
	
	def __init__(self, facebook_facade):
		print("Welcome to FacebookRedis Data Gathering")
		self.facebook_facade = facebook_facade	

	def save_all_posts_from_a_page_in_a_pile(self):
		page_id = input("Please, enter page id")
		page_alias = input("Please, insert page alias for database")
		self.facebook_facade.get_all_posts_from_page(page_id, page_alias)

	def saves_all_comments_from_unsaved_posts_pile(self):
		page_alias = input("Please, insert page alias to be gathered")
		self.facebook_facade.get_all_comments_from_posts_pile(page_alias)
