from source.controllers.facebook_controller import FacebookController

def main():
	facebook_facade = FacebookFacade()
	controller = FacebookController(facebook_facade)
	controller.save_all_posts_from_a_page_in_a_pile()

if __name__ == "__main__":
	main()

