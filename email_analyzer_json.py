import email.utils
from email.parser import Parser
import pandas as pd
from datetime import datetime

import json

class EmailAnalyzer:
	def __init__(self):
		self.data = {}

	def parse(self, email):
		
		email = Parser().parsestr(email)
    
	    ## If statement to catch variations in the TO, including restricted enron lists
		# tmp_to_email_list = []
		to_email_list = []
		from_email_list = []
		email_body = []
		date_time = []

		if email['to']:
			email_to = email['to']
			email_to = email_to.replace("\n", "")
			email_to = email_to.replace("\t", "")
			email_to = email_to.replace(" ", "")
			email_to = email_to.split(",")
			for email_to_1 in email_to:
				to_email_list.append(email_to_1) 
			# to_email_list.append(tmp_to_email_list)
		else:
			to_email_list.append(None)
	
		## Appending the FROM
		from_email_list.append(email['from'])

		## Appending the BODY
		email_body = email.get_payload().replace("\n", " ")
		# print(email_body)

		## Appending the DATETIME
		datetime_obj = datetime.strptime(email['date'][:-6], '%a, %d %b %Y %H:%M:%S %z')
		date_time.append(str(datetime_obj))
		# date_time.append(email['date'])

		self.data = {
						"from": from_email_list, # email['from'],
						"to": to_email_list,
						"date_time": date_time, # email['date'],
						"body": email_body
					}

		return json.dumps(self.data)
