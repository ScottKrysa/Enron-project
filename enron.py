import os
from email.parser import Parser

import csv

"""
Mark the folder containing all of the emails
"""
rootdir = "/Users/Scott/Desktop/tensorflow_projects/maildir"

"""
Loop through all subfolders and count files for each
"""
# for directory, subdirectory, filenames in  os.walk(rootdir):
#     print(directory, subdirectory, len(filenames))

"""
Using Parser to open the emails
"""

raw_file_dir = "/Users/Scott/Desktop/tensorflow_projects/maildir/lay-k/all_documents/1."

# with open(raw_file_dir, "r") as f:
# 	data = f.read()

# email = Parser().parsestr(data)

# print("\n To: " , email['to'])
# print("\n From: " , email['from'])
# print("\n Subject: " , email['subject'])
# print("\n \n Body: " , email.get_payload())

to_email_list = []
from_email_list = []
email_body = []

def email_analyse(inputfile, to_email_list, from_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()
 
    email = Parser().parsestr(data)
 
    to_email_list.append(email['to'])
    from_email_list.append(email['from'])
 
    email_body.append(email.get_payload())

email_analyse(raw_file_dir, to_email_list, from_email_list, email_body)

"""
Writing a CSV file and testing writing data to it
"""

master_email_list = [['name_of_file', 'to_email_list', 'from_email_list', 'email_body'], \
			[raw_file_dir, to_email_list, from_email_list, email_body]]

f = open('enron_test.csv', 'w')

with f:

    writer = csv.writer(f)
    
    for row in master_email_list:
        writer.writerow(row)
