import facebook
import redis

class FacebookPostsFacade:
		
	def save_post_by_post_id(db, post, page_alias):
		try:
			db.set("posts:" + PAGE_ALIAS + ":unsaved:" + post["id"], post["message"])
		except KeyError:
			try:
				db.set("posts:" + PAGE_ALIAS + ":unsaved:" + post["id"], post["story"])
			except:
				db.set("posts:" + PAGE_ALIAS + ":unsaved:" + post["id"], "No message nor story")


	def iterate_and_save_posts(db, graph, posts, page_alias, graph):
		while True:
			[save_post_by_post_id(db=db, post=post) for post in posts['data']]
			
			try:
				posts = requests.get(posts['paging']['next']).json()
			
			except facebook.GraphAPIError:
				input("Invalid token. Please insert new one.")

