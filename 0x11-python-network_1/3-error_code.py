#!/usr/bin/python3
"""
Takes in a url , sends a request to the url and
displays the body of the response (decoded in utf-8)
handles urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
import urllib.request
import urllib.parse
import urllib.error
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        data = response.read().decode()
        print(data)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
