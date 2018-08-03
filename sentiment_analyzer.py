from get_pos_neg_words import GetPosNegWords as get_pn
import nltk
# from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

class SentimentAnalyzer:

	def __init__(self):
		self.data = {}

	def do_pos_sentiment_analysis(self, text_list):
		positive_words,negative_words = get_pn().get_pos_neg_words()
		from nltk import word_tokenize
		pos_results = []
		# neg_results = []
		cpos = cneg = lpos = lneg = 0
		for word in text_list:
			if word in positive_words:
				cpos+=1
			# if word in negative_words:
				# cneg+=1
		pos_results.append(cpos/len(text_list))
		# neg_results.append(cneg/len(text_list))
		return pos_results#, neg_results

	def do_neg_sentiment_analysis(self, text_list):
		positive_words,negative_words = get_pn().get_pos_neg_words()
		from nltk import word_tokenize
		# pos_results = []
		neg_results = []
		cpos = cneg = lpos = lneg = 0
		for word in text_list:
			# if word in positive_words:
				# cpos+=1
			if word in negative_words:
				cneg+=1
		# pos_results.append(cpos/len(text_list))
		neg_results.append(cneg/len(text_list))
		return neg_results

