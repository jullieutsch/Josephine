import facebook

class FacebookCommentsFacade():
	def __init__(self, db, graph):
		self.db = db
		self.graph = graph

	def iterate_and_save_comments_from_pile(self):
		unsaved_posts_list = self.get_posts_from_unsaved_comments_pile()
		self.iterate_posts_to_gather_comments(unsaved_posts_list)

	def get_posts_from_unsaved_comments_pile():
		return self.db.keys("posts:bozonaro:unsaved:*")

	def iterate_posts_to_gather_comments(self, unsaved_posts_list):
		pile_counting = 0;
	
		for post_key in unsaved_posts_list:
			post_id = self.get_post_id_from_key(post_key)
			self.save_comments_from_post(db, post_id)
			self.remove_from_unsaved_posts_list(db, post_id, get_single_post_id_from_post_key(post_id))

			pile_counting = progress_increment(pile_counting)

	def progress_increment(self, status):
		print("post number " + str(status) + "is saved!")
		return status + 1

	def get_post_id_from_key(self, post_key):
		post_key = post_key.decode("utf-8")
		return post_key.replace("posts:bozonaro:unsaved:", "")



	