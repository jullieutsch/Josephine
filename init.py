from source.controllers.facebook_controller import FacebookController

def main():
	controller = FacebookController()
	controller.save_all_posts_from_a_page_in_a_pile()

if __name__ == "__main__":
	main()

