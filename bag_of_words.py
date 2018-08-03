import nltk
# from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

class BagOfWords:

	def __init__(self):
		self.data = {}

	def get_tokens(self, email_body):
		stop_words = set(stopwords.words('english'))
		tokenizer = RegexpTokenizer(r'\w+')
		raw_tokens = tokenizer.tokenize(email_body)
		# raw_tokens = word_tokenize(email_body)
		# filtered_tokens = filter(lambda token: token not in stop_words, raw_tokens)
		filtered_tokens = [w for w in raw_tokens if not w in stop_words]
		
		for word in filtered_tokens:
			if len(word) < 4:
				filtered_tokens.remove(word)

		# top_10 = Counter(filtered_tokens).most_common(10)
		# self.data = top_10
		self.data = list(filtered_tokens)
		return self.data
	
"""
Not sure if the following works. It's more of a placeholder for the moment.
"""
	def top_ten(self, tokens):
		top_10 = Counter(tokens).most_common(10)
		self.data = top_10
		return self.data
	
