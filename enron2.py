import os
import email.utils
from email.parser import Parser
import csv
import pandas as pd

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
Parse the raw files for key elements
"""
to_email_list = []
from_email_list = []
email_body = []
date_time = []

def email_analyse(inputfile, to_email_list, from_email_list, email_body, date_time):
    
    ## Open file
    with open(inputfile, "r") as f:
        data = f.read()

    ## Parse the file
    email = Parser().parsestr(data)
    
    ## If statement to catch variations in the TO, including restricted enron lists
    tmp_to_email_list = []
    if email['to']:
        email_to = email['to']
        email_to = email_to.replace("\n", "")
        email_to = email_to.replace("\t", "")
        email_to = email_to.replace(" ", "")
        email_to = email_to.split(",")
        for email_to_1 in email_to:
            tmp_to_email_list.append(email_to_1) 
        to_email_list.append(tmp_to_email_list)
    else:
        to_email_list.append(None)
    
    ## Appending the FROM
    from_email_list.append(email['from'])

    ## Appending the BODY
    email_body.append(email.get_payload())
    
    ## Appending the DATETIME
    date_time.append(email['date'])

"""
Calling the function, and testing if the # of elements are the same
"""
for filename in email_filenames:
    email_analyse(filename, to_email_list, from_email_list, email_body, date_time)

# assert len(email_filenames) = len(to_email_list)
# assert len(email_filenames) = len(from_email_list)
# assert len(email_filenames) = len(email_body)
# assert len(email_filenames) = len(date_time)

email_df = pd.DataFrame(
    {'email_filename': email_filenames,
     'to_email_list': to_email_list,
     'from_email_list': from_email_list,
     'email_body': email_body,
     'date_time': date_time
    })

# return: email_df


