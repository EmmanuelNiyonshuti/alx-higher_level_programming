#!/usr/bin/python3
"""
makes a request to https://alx-intranet.hbtn.io/status.
must use the package requests.
"""
import requests
if __name__ == "__main__":

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(str(r)))
    print("\t- content:", r.content.decode('utf-8'))
