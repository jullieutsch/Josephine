import facebook
import redis
from source.modules.facebook_post_facade import FacebookPostFacade

class FacebookFacade():

	def __init__ (self):
		first_access_token = input("Please insert app token")
		self.graph = facebook.GraphAPI(first_access_token)
		self.db = redis.StrictRedis()


	def get_all_posts_from_page(self, page_id):
		posts = new FacebookPostsFacade(self.get_page_posts(page_id))

	def get_page_posts(self,page_id):
		try:
			self.graph.get_object(page_id)
			return graph.get_connections(page['id'], 'posts', limit=500)
		except facebook.GraphAPIError:
			raise ValueError()



