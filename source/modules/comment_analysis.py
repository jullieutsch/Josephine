import datetime

def get_comments_occurrence(db, some_alias):
	full_results = db.keys("comments:" + some_alias + "*")

	for comment_key in full_results:
		comment = db.hmget(comment_key, "created_at")
		comment_date = get_comment_date(comment)

def get_comment_date(comment_datetime_str):
	comment_datetime = datetime.datetime.strptime(
		comment_datetime_str, '%Y-%m-%dT%H:%M:%S+%f')
	return comment_datetime.date()
