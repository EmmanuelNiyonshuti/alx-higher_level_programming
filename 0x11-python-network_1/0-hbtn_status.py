#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
    using the package urllib
"""
import urllib.request as request

url = "https://alx-intranet.hbtn.io/status"
req = request.Request(url)
with request.urlopen(req) as response:
    data = response.read()
print("Body response:")
print("\t-type:", type(data))
print("\t-type:", data)
print("\t-utf8 content:", data.decode('utf-8'))
