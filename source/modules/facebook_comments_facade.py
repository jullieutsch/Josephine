import facebook
from modules.models.facebook_comment import FacebookComment
from modules.models.facebook_post import FacebookPost

class FacebookCommentsFacade():
	def __init__(self, db, graph):
		self.db = db
		self.graph = graph
		self.facebook_comment = FacebookComment()
		self.facebook_post = FacebookPost()

	def iterate_and_save_comments_from_pile(self, page_alias):
		unsaved_posts_list = facebook_post.get_posts_from_unsaved_comments_pile(self.db, page_alias)
		self.iterate_posts_to_gather_comments(unsaved_posts_list, page_alias)

	def iterate_posts_to_gather_comments(self, unsaved_posts_list, page_alias):
		pile_counting = 0;
	
		for post_key in unsaved_posts_list:
			post_id = self.facebook_post.get_post_id_from_key(post_key)
			self.iterate_and_save_comments_from_post(post_key)
			self.remove_from_unsaved_posts_list(db, 
				post_id, self.facebook_post.get_single_post_id_from_post_key(post_id), page_alias)

			pile_counting = self.progress_increment(pile_counting)

	def progress_increment(self, status):
		print("post number " + str(status) + "is saved!")
		return status + 1

	def remove_from_unsaved_posts_list(db, single_post_id, page_alias):
		if self.facebook_comment.are_comments_saved(db, single_post_id, page_alias):
			self.facebook_posts.change_post_status_for_saved_comments(db, single_post_id, page_alias)

	def iterate_and_save_comments_from_post(post_id):
		pipeline = self.db.pipeline()
		comments = self.graph.get_connections(id=post_id, connection_name='comments', limit=500)
		while True:
			try:
				[self.facebook_comment.save(pipeline=pipeline, comment=comment) for comment in comments['data']]
				comments = requests.get(comments['paging']['next']).json()
			except KeyError:
				pipeline.execute()
				print("+ 500 saved comments")
				break   

	