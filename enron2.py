import os
from email.parser import Parser

"""
Mark the folder containing all of the emails
"""
rootdir = "/Users/Scott/Desktop/tensorflow_projects/maildir"

"""
Loop through all subfolders and count files for each
"""
for directory, subdirectory, filenames in  os.walk(rootdir):
    print(directory, subdirectory, len(filenames))

"""
Define a function to analyze the email headers and create lists from them
"""
# def email_analyse(inputfile, to_email_list, from_email_list, email_body):
#     with open(inputfile, "r") as f:
#         data = f.read()
 
#     email = Parser().parsestr(data)
 
#     to_email_list.append(email['to'])
#     from_email_list.append(email['from'])
 
#     email_body.append(email.get_payload())

# to_email_list = []
# from_email_list = []
# email_body = []

# for directory, subdirectory, filenames in  os.walk(rootdir):
#     for filename in filenames:
#         email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )

# print(to_email_list[0:5])
# print(from_email_list[0:5])
# print(email_body[0:1])