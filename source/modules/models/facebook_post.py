class FacebookPost:
	
	def save_post_by_post_id(self, db, post, page_alias):
		try:
			db.set("posts:" + page_alias + ":unsaved:" + post["id"], post["message"])
		except KeyError:
			try:
				db.set("posts:" + page_alias + ":unsaved:" + post["id"], post["story"])
			except:
				db.set("posts:" + page_alias + ":unsaved:" + post["id"], "No message nor story")

	def change_post_status_for_saved_comments(self, db, page_alias, post_complete_id):
		db.set("posts:" + page_alias + ":saved:" + post_complete_id, 
			self.get_single_post_id_from_post_key(post_complete_id))

		db.delete("posts:" + page_alias + ":unsaved:" + post_complete_id)

	def get_posts_from_unsaved_comments_pile(self, db, page_alias):
		return db.keys("posts:" + page_alias + ":unsaved:*")

	def get_single_post_id_from_post_key(self, post_id):
		return 	post_id.split("_")[1]

	def get_post_id_from_key(self, post_key, page_alias):
		post_key = post_key.decode("utf-8")
		return post_key.replace("posts:" + page_alias + ":unsaved:", "")