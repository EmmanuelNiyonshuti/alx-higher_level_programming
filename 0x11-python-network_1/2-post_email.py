#!/usr/bin/python3
"""
takes in a url and makes a POST request to the passed url
with an E-mail as a parameter.
"""
import urllib.request
import urllib.parse
import sys

if __name__=="__main__":
    email = sys.argv[2]

    email = urllib.parse.urlencode({'email': email})
    email = email.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data=email, method='POST')

    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
    print(data)
