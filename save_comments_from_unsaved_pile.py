import facebook
import redis
import requests

def save_comment_content(db, comment):
	try:
		db.set("comments:saved:" + comment["id"], comment["message"])
	except KeyError:
		print(comment)

def get_post_id_from_key(post_key):
	post_key = post_key
	return post_key.replace("comments:unsaved:", "")

def get_single_post_id_from_post_key(post_id):
	return 	post_id.split("_")[1]

def iterate_unsaved_pile_and_save_comments():
	db = redis.StrictRedis()
	iterate_unsaved_posts_pile(db)

def are_comments_saved(db, post_id):
	keys = db.keys("comments:saved:" + post_id + "*")
	return len(keys)

def remove_from_unsaved_posts_list(db, post_id, single_post_id):
	if are_comments_saved(db, single_post_id):
		db.delete("comments:unsaved:" + post_id)

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def iterate_unsaved_posts_pile(db):
	unsaved_posts_list = db.keys("comments:unsaved:*")

	for post_key in unsaved_posts_list:
		post_key = post_key.decode("utf-8")
		post_id = get_post_id_from_key(post_key)
		save_comments_from_post(db, post_id)
		remove_from_unsaved_posts_list(db, post_id, get_single_post_id_from_post_key(post_id))
		print("Post finalizado: " + post_id)

def iterate_and_save_comments(db, graph, post_id):
	comments = graph.get_connections(id=post_id, connection_name='comments', limit=500)
	while True:
		try:
			[save_comment_content(db=db, comment=comment) for comment in comments['data']]
			comments = requests.get(comments['paging']['next']).json()    
		except KeyError:
			break

def save_comments_from_post(db, post_key):
	access_token = """EAACEdEose0cBAFvitXJ8ZCUO05hpXMWnZCFWSN8OEZCE3cYOv2HqfBU5GABHBteyTkfTL90rPPztsTJTN0K4lSiauVfOZAROqXlsmZCrVkEV6sCeOOVdiVaes2nZA7EUKpnjNBZASsGIdaemjCDnurViSDPlOATCfAXWLfDX2DWLIQZBal2NeNSZB26axhC9ot8B9dFmK9j81CwZDZD"""
	graph = define_graph_from_token(access_token)
	iterate_and_save_comments(db, graph, post_key)

def main():
	iterate_unsaved_pile_and_save_comments()

if __name__ == "__main__":
    main()