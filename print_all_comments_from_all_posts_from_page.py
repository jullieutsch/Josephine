import facebook
import requests

def print_object_title_or_data(fb_object):
	try:
		print(fb_object["message"])
	except KeyError:
		print(fb_object)

def print_post_title_and_comments(post, graph):
	print_object_title_or_data(post)
	iterate_and_print_comments_from_post(post["id"], graph)

def iterate_and_print_comments_from_post(post_id, graph):
	comments = graph.get_connections(id=post_id, connection_name='comments', limit=500)
	while True:
		try:
			[print_object_title_or_data(fb_object=comment) for comment in comments['data']]
			comments = requests.get(comments['paging']['next']).json()    
		except KeyError:
			break

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def print_all_posts_titles_from_certain_page():
	access_token = """EAACEdEose0cBAFjt1b2wLvw182wX2qRtzjlZCgqm1rZBSlpHMaJsRZACFEAP8
	bbyesCPj3qaS34Jm5UX6EuJ37WcvzHk9nJkwQye5cR4b76EQYUnMvvhT4sAzbIenVkE6ZAp3wd6bo89jK9FEc10SQIpmaOmUo8oALGgrtHZA3xOmJfO39EUhsn04uCulUSy382z0N3AnkwZDZD"""
	page_id = "211857482296579"
	graph = define_graph_from_token(access_token)
	page = set_page_from_graph(graph, page_id)

	print_all_pages_titles_and_comments(graph, page)

def print_all_pages_titles_and_comments(graph, page):
	posts = graph.get_connections(page['id'], 'posts', limit=100)
	while True:
		try:
			[print_post_title_and_comments(post=post, graph=graph) for post in posts['data']]
			posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			break

def set_page_from_graph(graph, page_id):
	return graph.get_object(page_id)

def main():
	print_all_posts_titles_from_certain_page();

if __name__ == "__main__":
    main()



