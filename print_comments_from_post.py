import facebook
import requests

def print_post_title(comment):
	try:
		print(comment["message"])
	except KeyError:
		print(comment)

def define_graph_from_token(access_token):
	return facebook.GraphAPI(access_token)

def print_all_comments_from_a_post():
	access_token = """EAACEdEose0cBAFjt1b2wLvw182wX2qRtzjlZCgqm1rZBSlpHMaJsRZACFEAP8bbyesCPj3qaS34Jm5UX6EuJ37WcvzHk9nJkwQye5
	cR4b76EQYUnMvvhT4sAzbIenVkE6ZAp3wd6bo89jK9FEc10SQIpmaOmUo8oALGgrtHZA3xOmJfO39EUhsn04uCulUSy382z0N3AnkwZDZD"""

	post_id = "924943247654662"
	graph = define_graph_from_token(access_token)
	
	print_all_comments(graph, post_id)

def print_all_comments(graph, post_id):
	comments = graph.get_connections(id=post_id, connection_name='comments', limit=500)
	while True:

		try:
			[print_post_title(comment=comment) for comment in comments['data']]
			comments = requests.get(comments['paging']['next']).json()    
		except KeyError:
			break

def main():
	print_all_comments_from_a_post();

if __name__ == "__main__":
    main()
