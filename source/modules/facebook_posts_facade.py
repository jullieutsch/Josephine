import facebook
import redis
import requests
from modules.models.facebook_post import FacebookPost

class FacebookPostsFacade:
	
	def iterate_and_save_posts(self, db, graph, posts, page_alias):
		facebook_post = FacebookPost()
		while True:
			[facebook_post.save_post_by_post_id(db=db, post=post, page_alias=page_alias) for post in posts['data']]
			
			try:
				posts = requests.get(posts['paging']['next']).json()
			
			except facebook.GraphAPIError:
				input("Invalid token. Please insert new one.")

