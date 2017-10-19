import facebook
import requests
import redis

def save_post_title_by_post_id(db, post):
	try:
		db.set("comments:unsaved:" + post["id"], post["message"])
	except KeyError:
		try:
			db.set("comments:unsaved:" + post["id"], post["story"])
		except:
			db.set("comments:unsaved:" + post["id"], "No message nor story")



def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def print_all_posts_titles_from_certain_page(): 
	graph = define_graph_from_token("""EAACEdEose0cBAKBcJ1ZAb1EnAJYPI5q5vGEdyaZC5oETHkMEovfXdQWKT8e4f8ZCqZBRCD3vRXSKM2STnyOvupNmmtSbqgW4LeJWKDUZAryLttotTevtGmZAKy5FbXogROOQPhePBcuxyM4XuT6z3THl2xbEpZBXYX99ZBC1A0Ty13es85P9ggCaLZBKZBEYc9hT4MiSfZB8J39YgZDZD""")
	page = set_page_from_graph(graph, page_id= "211857482296579")
	db = redis.StrictRedis()

	print_all_pages_titles(db, graph, page)

def print_all_pages_titles(db, graph, page):
	posts = graph.get_connections(page['id'], 'posts', limit=100)
	while True:
		try:
			[save_post_title_by_post_id(db=db, post=post) for post in posts['data']]
			posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			break

def set_page_from_graph(graph, page_id):
	return graph.get_object(page_id)

def main():
	print_all_posts_titles_from_certain_page();

if __name__ == "__main__":
    main()



