import redis;

class TextAppender():
	def iterate_comments_and_save_text(self, comments, db):
		stats_counter = 0
		pipeline = db.pipeline()
		thousands = 1
		for comment_key in comments:
			comment_text= db.hget(comment_key, "message").decode("utf-8")
			pipeline.append("bolsonaro_comments_complete_31_05_2018", comment_text)
			stats_counter = stats_counter + 1
			if(stats_counter == 10001):
				stats_counter = 0
			if(stats_counter==10000):
				pipeline.execute()
				print("Comentários salvos: ")
				print(thousands * 10000)
				print( "\n \n")
				thousands = thousands + 1

		pipeline.execute()

	def save_comments_as_text(self, db):
		comments = db.keys("comments:bolsonaro_31_05*")
		self.iterate_comments_and_save_text(comments, db)