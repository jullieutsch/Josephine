from modules.facebook_facade import FacebookFacade
from modules.text_appender import TextAppender
import modules.vocabulary
import modules.comment_analysis
import modules.csv_generator

class FacebookController:
	
	def __init__(self, facebook_facade):
		print("Welcome to FacebookRedis Data Gathering")
		self.facebook_facade = facebook_facade
		self.vocabulary = modules.vocabulary
		self.comment_analysis = modules.comment_analysis
		self.csv_generator = modules.csv_generator

	def save_all_posts_from_a_page_in_a_pile(self):
		page_id = input("Please, enter page id")
		page_alias = input("Please, insert page alias for database")
		self.facebook_facade.get_all_posts_from_page(page_id, page_alias)

	def saves_all_comments_from_unsaved_posts_pile(self):
		page_alias = input("Please, insert page alias to be gathered")
		self.facebook_facade.get_all_comments_from_posts_pile(page_alias)

	def append_comments_in_single_corpus(self):
		TextAppender().save_comments_as_text(self.facebook_facade.db)

	def generate_word_cloud(self):
		self.vocabulary.generate_word_cloud(self.facebook_facade.db)

	def generate_csv_for_comment_ocurrence_on_corpus(self):
		page_alias  = input("Please, enter page alias")
		comments_ocurrence = self.comment_analysis.get_comments_occurrence(self.facebook_facade.db, page_alias)
		self.csv_generator.generate_csv_from_dict(comments_ocurrence)

		


