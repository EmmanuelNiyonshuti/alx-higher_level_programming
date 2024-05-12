#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
    using the package urllib
"""
import urllib.request as request

url = "https://alx-intranet.hbtn.io/status"
req = request.Request(url)
with request.urlopen(req) as response:
    body = response.read()

print(f"Body response:\n"
      f"    - type: {type(body)}\n"
      f"    - content: {body}\n"
      f"    - utf8 content: {body.decode()}")
