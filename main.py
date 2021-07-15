# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:15:17 2021

@author: SHUBHAM
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:15:17 2021

@author: SHUBHAM
"""

target="flipkart.com"

#TOPOLOGY
from webb import webb
print(webb.traceroute(target,"flipkart_topology.txt"))
webb.ping(target)
#webb.get_ip(target)


import whois
w = whois.whois('flipkart.com')
w.expiration_date
w.text

import subprocess
output = subprocess.Popen("ping flipkart.com", shell=True, stdout=subprocess.PIPE).stdout.read()
print(output)


#SUBDOMAIN
subprocess.Popen("python subscraper.py -e 3  flipkart.com", shell=True, stdout=subprocess.PIPE).stdout.read()

subprocess.Popen("amass enum -passive -d flipkart.com -src", shell=True, stdout=subprocess.PIPE).stdout.read()


#AWS BUCKETS
import requests
url="https://buckets.grayhatwarfare.com/api/v1/files/flipkart.in?access_token=e5289aeee79cbc1b9d4a312bd0cb6e38"
resp = requests.get(url)
import ast
dict_str = (resp.content).decode("UTF-8")
mydata = ast.literal_eval(dict_str)
