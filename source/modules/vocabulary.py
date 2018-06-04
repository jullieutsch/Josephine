from nltk import FreqDist, sent_tokenize, word_tokenize
import string
from modules.tokenizer import tokenize_without_punctuation
import redis
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(db):
	with open('stopwords.txt') as file:
		stopwords = str(file.read())
	stopwords = tokenize_without_punctuation(stopwords)

	print("montando stopwords")

	#with open('comments_menor.txt') as file:
	#    textbolso = str(file.read())
	textbolso = db.get("bolsonaro_comments_complete_31_05_2018").decode("utf-8")

	print("corpus do banco baixado.")

	words = tokenize_without_punctuation(textbolso)

	print("palavras tokenizadas")

	filtered_words = [word for word in words if word not in stopwords]

	print("palavras filtradas")

	most_common = FreqDist(map(str.casefold, filtered_words)).most_common(1000)

	print("palavras mais comuns mapeadas")

	print("desenhando nuvem!")

	wordcloud = WordCloud(collocations=False, width = 1520, height = 535).generate_from_frequencies(dict(most_common))
	plt.figure(figsize=(16,9))
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


