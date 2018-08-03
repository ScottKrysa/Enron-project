
class GetPosNegWords:

	def __init__(self):
		self.data = {}

	def get_pos_neg_words(self):
		def get_words(url):
			import requests
			words = requests.get(url).content.decode('latin-1')
			word_list = words.split('\n')
			index = 0
			while index < len(word_list):
				word = word_list[index]
				if ';' in word or not word:
					word_list.pop(index)
				else:
					index+=1
			return word_list

		#Get lists of positive and negative words
		p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
		n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
		positive_words = get_words(p_url)
		negative_words = get_words(n_url)
		return positive_words,negative_words