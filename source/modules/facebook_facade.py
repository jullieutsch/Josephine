import facebook
import redis
from modules.facebook_posts_facade import FacebookPostsFacade

class FacebookFacade():

	def __init__ (self):
		first_access_token = input("Please insert app token")
		self.graph = facebook.GraphAPI(first_access_token)
		self.db = redis.StrictRedis()


	def get_all_posts_from_page(self, page_id, page_alias):
		posts = FacebookPostsFacade(self.db, self.graph, 
			self.get_page_posts(page_id), 
			page_alias)

	def get_page_posts(self, page_id):
		try:
			page = self.graph.get_object(page_id)
			return self.graph.get_connections(page['id'], 'posts', limit=100)
		except facebook.GraphAPIError:
			raise ValueError()



