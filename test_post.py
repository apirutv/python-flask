#!/usr/bin/env python3

import requests

remote_url = "http://192.168.1.182:5000/first_call?id=12345
post_data = {'name','Art'}

r = requests.post(remote_url,post_data)
print(r.status, r.reason)
print(r.text)
