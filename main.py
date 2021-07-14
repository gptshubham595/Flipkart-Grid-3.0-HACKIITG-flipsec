# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:15:17 2021

@author: SHUBHAM
"""

target="flipkart.in"

from webb import webb
print(webb.traceroute(target,"flipkart_topology.txt"))
webb.ping(target)
webb.get_ip(target)



import whois
w = whois.whois('flipkart.in')
w.expiration_date
w.text

import sublist3r 
subdomains = sublist3r.main('flipkart.in', 40, 'subdomains.txt', ports= None,
                            silent=False, verbose= False, enable_bruteforce= False,
                            engines=None)


#BUCKETS
import requests
url="https://buckets.grayhatwarfare.com/api/v1/files/flipkart.in?access_token=e5289aeee79cbc1b9d4a312bd0cb6e38"
resp = requests.get(url)
import ast
dict_str = (resp.content).decode("UTF-8")
mydata = ast.literal_eval(dict_str)
