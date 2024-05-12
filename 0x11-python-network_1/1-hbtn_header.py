#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id
    variable found in the header of the response.
"""

import urllib.request as request
import sys

with request.urlopen(sys.argv[1]) as response:
    """print(dir(response))"""
    print(response.getheader('X-Request-Id', None))
