class FacebookComment:
	
	def __init__(self, db, comment_data):
		self.db = db
		self.comment_map = { 
			"id": comment_data["id"],
			"message": comment_data["message"], 
			"created_time":comment_data["created_time"]}

	def save():
		db.hmset("comments::saved:" + comment_map["id"], comment_map)

