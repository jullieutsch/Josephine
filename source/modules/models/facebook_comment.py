class FacebookComment:
	
	def save(self, db, page_alias, comment_data):
		comment_map = { 
			"id": comment_data["id"],
			"message": comment_data["message"], 
			"created_time":comment_data["created_time"]}

		db.hmset("comments:" + page_alias + ":saved:" + comment_map["id"] , comment_map)

	def are_comments_saved(self, db, page_alias, post_id):
		keys = db.keys("comments:"+ page_alias + ":saved:" + post_id + "*")
		return len(keys)

