import requests
import sys
import json
from json import dumps
from datetime import datetime
from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self,message):
		token_dict = {'access_token':'xoxp-569934227830-706838758277-739508525463-62b8c5de18b25a0a95bfd0bc9cd864ad'}
		auth_token = token_dict['access_token']
		url = "https://slack.com/api/chat.postMessage"
		payload = {"channel": "CGQB47LKV",
		  					"text": message
		  					}
		header = {'Content-Type': 'application/json',
					'Accept': 'application/json',
		          'Authorization' : 'Bearer {0}'.format(auth_token)
		        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)



