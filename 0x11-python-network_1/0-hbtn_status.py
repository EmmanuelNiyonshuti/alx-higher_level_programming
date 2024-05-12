#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
    using the package urllib
"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        data = response.read()
    print("Body response:")
    print("\t-type:", type(data))
    print("\t-type:", data)
    print("\t-utf8 content:", data.decode('utf-8'))
