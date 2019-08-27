import sys
import requests

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
       try:
       		 res = requests.get(url)
		 print(res.url)
                 print(res.status_code)
       except requests.exceptions.MissingSchema:
		 print("invalid url")
		 sys.exit(0)
