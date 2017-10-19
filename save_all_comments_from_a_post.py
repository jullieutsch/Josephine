import facebook
import requests
import redis

def save_comment_content(db, comment):
	try:
		db.set("comments:saved:" + comment["id"], comment["message"])
		print(comment)
	except KeyError:
		print(comment)

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def save_all_comments_from_a_post():
	access_token = """EAACEdEose0cBAFxJZBlI8F73ZAOSLtpSRY8d2arbgUsbiBMcgHRS7DV83DVZCRkYQ94ZC22cRvJwWqa1hwztOaAEOpUP6RNwIBsZBPT2Iq8q6dGMKfg0ZBx7hhv1Jb1DOAnNPTTd5VZCRQ3kQ5XFm4aHoBgk7HVkZBkVtzIbEYRAu8OzTppcz3CoY7tmZAoCTrH8ZD"""

	post_id = "933471936801793"
	graph = define_graph_from_token(access_token)

	db = redis.StrictRedis()
	
	iterate_and_save_comments_from_post(db, graph, post_id)

def iterate_and_save_comments_from_post(db, graph, post_id):
	comments = graph.get_connections(id=post_id, connection_name='comments', limit=500)
	while True:

		try:
			[save_comment_content(db=db, comment=comment) for comment in comments['data']]
			comments = requests.get(comments['paging']['next']).json()    
		except KeyError:
			break

def main():
	save_all_comments_from_a_post();

if __name__ == "__main__":
    main()