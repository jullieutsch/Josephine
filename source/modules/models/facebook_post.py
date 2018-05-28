class FacebookPost:
	
	def change_post_status_for_saved_comments(db, page_alias, post_id):
		db.delete("posts:" + page_alias + ":unsaved:" + post_id)
		db.set("posts:" + page_alias + ":saved:" + post_id, post_id)

	def get_posts_from_unsaved_comments_pile(db, page_alias):
		return db.keys("posts:" + page_alias + ":unsaved:*")

	def get_single_post_id_from_post_key(post_id):
		return 	post_id.split("_")[1]

	def get_post_id_from_key(self, post_key):
		post_key = post_key.decode("utf-8")
		return post_key.replace("posts:" + post_key + ":unsaved:", "")