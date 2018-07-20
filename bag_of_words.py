import nltk
from nltk import word_tokenize
from collections import Counter

class BagOfWords:

	def __init__(self):
		self.data = {}

	def get_tokens(self, email_body):
		tokens = word_tokenize(email_body)
		top_10 = Counter(tokens).most_common(10)

		return top_10