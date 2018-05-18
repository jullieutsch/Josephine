import facebook
import redis
import requests

class FacebookPostsFacade:
	
	def __init__(self, db, graph, posts, page_alias):	
		self.iterate_and_save_posts(db, graph, posts, page_alias)

	def save_post_by_post_id(self, db, post, page_alias):
		try:
			db.set("posts:" + page_alias + ":unsaved:" + post["id"], post["message"])
		except KeyError:
			try:
				db.set("posts:" + page_alias + ":unsaved:" + post["id"], post["story"])
			except:
				db.set("posts:" + page_alias + ":unsaved:" + post["id"], "No message nor story")


	def iterate_and_save_posts(self, db, graph, posts, page_alias):
		while True:
			[self.save_post_by_post_id(db=db, post=post, page_alias=page_alias) for post in posts['data']]
			
			try:
				posts = requests.get(posts['paging']['next']).json()
			
			except facebook.GraphAPIError:
				input("Invalid token. Please insert new one.")

