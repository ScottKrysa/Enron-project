import os
import csv
import pandas as pd
from pandas.io.json import json_normalize
from email_analyzer_pd import EmailAnalyzer
from bag_of_words import BagOfWords
from sentiment_analyzer import SentimentAnalyzer
import json

import pprint
pp = pprint.PrettyPrinter(indent=4)


"""
Mark the folder containing all of the emails
"""


rootdir = "/Users/Scott/Desktop/tensorflow_projects/maildir_test"


"""
Loop through all subfolders and get the filenames for each
"""


email_filenames = []

for dirpath, subdirs, files in os.walk(rootdir):
	for file in files:
		if not file.startswith('.'):     # Ignore hidden files
			email_filenames.append(os.path.join(dirpath, file))


"""
Loop through through the files and create a 
Pandas Database using EmailAnalyzer()
"""


email_list = []

try:
	for filename in email_filenames:
		with open(filename, "r") as f:
			data = f.read() 
		df_tmp = EmailAnalyzer().parse(data)
		email_list.append(df_tmp)
except:
	pass

df = pd.DataFrame(email_list)

df.columns=['from','to','date','body']


"""
Converting dates from lists to raw datetimes
"""


datetime_list = []
for x in range(len(df)):
	datetime_obj = df['date'][x][0]
	datetime_list.append(datetime_obj)

df['datetime'] = datetime_list
df['datetime'] = pd.to_datetime(df['datetime'], utc=True)
# df = df.set_index('datetime')
df = df.drop(['date'], axis=1)
# df.sort_index(inplace=True)

# pp.pprint(df)


"""
Apply BagOfWords() to each body of 
"""

token_list = []

for x in range(len(df)):
	tokens = BagOfWords().get_tokens(df['body'][x][0])
	token_list.append(tokens)

df['body_tokens'] = token_list

# pp.pprint(df)


"""
Iterate through the files and count words in body
"""

token_list = []

for x in range(len(df)):
	tokens = BagOfWords().get_tokens(df['body'][x][0])
	token_list.append(tokens)

df['body_tokens'] = token_list

# pp.pprint(df)


"""
SentimentAnalyzer
"""


sa = SentimentAnalyzer()
# print(sa.do_pos_sentiment_analysis(df['body_tokens'][0]))
# print(sa.do_neg_sentiment_analysis(df['body_tokens'][0]))

pos_sent_list = []
for x in range(len(df)):
    pos_sent_result = sa.do_pos_sentiment_analysis(df['body_tokens'][x])
    pos_sent_list.append(pos_sent_result[0])
    
df['% Positive'] = pos_sent_list

neg_sent_list = []
for x in range(len(df)):
    neg_sent_result = sa.do_neg_sentiment_analysis(df['body_tokens'][x])
    neg_sent_list.append(neg_sent_result[0])
    
df['% Negative'] = neg_sent_list

pp.pprint(df)
