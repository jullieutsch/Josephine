import facebook
import requests
import redis

def save_key(db, fb_object_type, key, value):
	db.hset(fb_object_type, key, value)

def save_object_title_or_message(db, fb_object, fb_object_type):
	try:
		save_key(db, fb_object_type, fb_object["id"], fb_object["message"])
	except KeyError:
		print("segue o baile")	

def iterate_and_save_comments_from_post(db, post_id, graph):
	comments = graph.get_connections(id=post_id, connection_name='comments', limit=500)
	while True:
		try:
			[save_object_title_or_message(db, fb_object=comment, fb_object_type=post_id) for comment in comments['data']]
			comments = requests.get(comments['paging']['next']).json()  
		except KeyError:
			break

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def set_page_from_graph(graph, page_id):
	return graph.get_object(page_id)

def save_post_title_and_comments(db, post, graph):
	save_object_title_or_message(db, post, "post")
	iterate_and_save_comments_from_post(db, post["id"], graph)

def iterate_posts(graph, page, db):
	posts = graph.get_connections(page['id'], 'posts', limit=100)	
	while True:
		try:
			[save_post_title_and_comments(db=db, post=post, graph=graph) for post in posts['data']]
			posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			break

def save_all_comments_and_posts_from_a_page():
	access_token = """EAACEdEose0cBAHZA2hIff857kdN5iPQN8LxilcFEdt3LWd2ZA3ipRockbwyqOhxnwjXJOcNb8xSlqGiZBZCUeSwJ5opLtGJ0JhOKN4y1ZBirf2gMqpWQSaC3Q5jK3FZBl6OMnAwCNtVNPc08mSswrgf7LykfjlxNZBWoBshSnxfg8zbBZB0aKzovcN0PmIEijkknhfgN0ZAp4WQZDZD"""
	graph = define_graph_from_token(access_token)
	page = set_page_from_graph(graph, "211857482296579")
	db = redis.StrictRedis()
	iterate_posts(graph, page, db)

def main():
	save_all_comments_and_posts_from_a_page();

if __name__ == "__main__":
    main()



