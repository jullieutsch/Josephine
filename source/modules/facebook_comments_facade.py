import facebook
from modules.models.facebook_comment import FacebookComment
from modules.models.facebook_post import FacebookPost
import requests

class FacebookCommentsFacade():
	def __init__(self, db, graph):
		self.db = db
		self.graph = graph
		self.facebook_comment = FacebookComment()
		self.facebook_post = FacebookPost()

	def iterate_and_save_comments_from_pile(self, page_alias):
		unsaved_posts_list = self.facebook_post.get_posts_from_unsaved_comments_pile(self.db, page_alias)
		self.iterate_posts_to_gather_comments(unsaved_posts_list, page_alias)

	def iterate_posts_to_gather_comments(self, unsaved_posts_list, page_alias):
		pile_counting = 0;
	
		for post_key in unsaved_posts_list:
			complete_post_id = self.facebook_post.get_post_id_from_key(post_key, page_alias)
			self.iterate_and_save_comments_from_post(page_alias, complete_post_id)
			self.remove_from_unsaved_posts_list(self.db, 
				page_alias, complete_post_id)

			pile_counting = self.progress_increment(pile_counting)

	def progress_increment(self, status):
		print("post number " + str(status) + "is saved!")
		return status + 1

	def remove_from_unsaved_posts_list(self, db, page_alias, complete_post_id):
		if self.facebook_comment.are_comments_saved(db, page_alias, 
			self.facebook_post.get_single_post_id_from_post_key(complete_post_id)):
				self.facebook_post.change_post_status_for_saved_comments(db, page_alias, complete_post_id)

	def iterate_and_save_comments_from_post(self, page_alias, post_id):
		pipeline = self.db.pipeline()
		comments = self.graph.get_connections(id=post_id, connection_name='comments', limit=500)
		while True:
			try:
				[self.facebook_comment.save(db=pipeline, page_alias= page_alias, comment_data=comment) for comment in comments['data']]
				print("+ 500 saved comments")
				comments = requests.get(comments['paging']['next']).json()
			except KeyError:
				pipeline.execute()
				break   

	