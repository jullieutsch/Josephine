def get_comments_occurrence(db, some_alias):
	full_results = db.keys("comments:" + some_alias + "*")

	for comment_key in full_results:
		print("hi there")
		#comment_date = get_comment_date(comment)

def get_comment_date(comment):
	return comment
