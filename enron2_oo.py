import os
import csv
import pandas as pd
from pandas.io.json import json_normalize
from email_analyzer import EmailAnalyzer
import json

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
Calling the function, and testing if the # of elements are the same
"""
for filename in email_filenames:

	with open(filename, "r") as f:
		data = f.read()
	# tmp = EmailAnalyzer().parse(data)
	# print(tmp)
	email_df = json_normalize(json.loads(EmailAnalyzer().parse(data)))

	print(email_df)





