import os
import csv
import pandas as pd
from pandas.io.json import json_normalize
from email_analyzer_pd import EmailAnalyzer
from bag_of_words import BagOfWords
import json

import pprint


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

email_df = pd.DataFrame(email_list)

email_df.columns=['from','to','date','body']


"""
Converting dates from lists to raw datetimes
"""


datetime_list = []
for x in range(len(email_df)):
	datetime_obj = email_df['date'][x][0]
	datetime_list.append(datetime_obj)

email_df['datetime'] = datetime_list
email_df['datetime'] = pd.to_datetime(email_df['datetime'], utc=True)
# email_df = email_df.set_index('datetime')
email_df = email_df.drop(['date'], axis=1)
# email_df.sort_index(inplace=True)


pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(email_df)


"""
Testing BagOfWords on a Sample Email Body
"""


# token_sample = BagOfWords().get_tokens(email_df['body'][0][0])

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(token_sample)
# print(list(token_sample))


"""
Iterate through the files and count words in body
"""


token_list = []

for x in range(len(email_df)):
	tokens = BagOfWords().get_tokens(email_df['body'][x][0])
	token_list.append(tokens)

email_df['body_tokens'] = token_list

pp.pprint(email_df)
