import facebook
import requests

def print_post_title(post):
	try:
		print(post["message"])
	except KeyError:
		print(post)

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def print_all_posts_titles_from_certain_page():
	access_token = """"""
	page_id = ""
	graph = define_graph_from_token(access_token)
	page = set_page_from_graph(graph, page_id)
	
	print_all_pages_titles(graph, page)

def print_all_pages_titles(graph, page):
	posts = graph.get_connections(page['id'], 'posts', limit=100)
	while True:
		try:
			[print_post_title(post=post) for post in posts['data']]
			posts = requests.get(posts['paging']['next']).json()    
		except KeyError:
			break

def set_page_from_graph(graph, page_id):
	return graph.get_object(page_id)

def main():
	print_all_posts_titles_from_certain_page();

if __name__ == "__main__":
    main()



