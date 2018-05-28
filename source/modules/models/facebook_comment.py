class FacebookComment:
	
	def save(self, db, comment_data):
		self.db = db
		self.comment_map = { 
			"id": comment_data["id"],
			"message": comment_data["message"], 
			"created_time":comment_data["created_time"]}

		db.hmset("comments::saved:" + self.comment_map["id"], self.comment_map)

	def are_comments_saved(db, post_alias, post_id):
		keys = db.keys("comments:"+ post_alias + ":saved:" + post_id + "*")
		return len(keys)

