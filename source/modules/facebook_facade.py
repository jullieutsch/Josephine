import facebook
import redis
from modules.facebook_posts_facade import FacebookPostsFacade
from modules.facebook_comments_facade import FacebookCommentsFacade

class FacebookFacade():

	def __init__ (self):
		first_access_token = input("Please insert app token")
		self.graph = facebook.GraphAPI(first_access_token)
		self.db = redis.StrictRedis()
		self.posts_facade = FacebookPostsFacade()
		self.comments_facade = FacebookCommentsFacade(self.db)

	def get_all_posts_from_page(self, page_id, page_alias):
		page_posts_connection = self.get_page_posts(page_id)
		self.posts_facade.iterate_and_save_posts(self.db, self.graph, 
			page_posts_connection, page_alias)

	def get_page_posts(self, page_id):
		try:
			page = self.graph.get_object(page_id)
			return self.graph.get_connections(page['id'], 'posts', limit=100)
		except facebook.GraphAPIError:
			raise ValueError()

	def get_all_comments_from_posts_pile(self):
		self.comments_facade.iterate_and_save_comments_from_pile()



