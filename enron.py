import os
from email.parser import Parser

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

with open(raw_file_dir, "r") as f:
	data = f.read()

email = Parser().parsestr(data)

print("\n To: " , email['to'])
print("\n From: " , email['from'])
print("\n Subject: " , email['subject'])
print("\n \n Body: " , email.get_payload())