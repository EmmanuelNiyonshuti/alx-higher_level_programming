#!/usr/bin/bash
#sends a request to a url and displays the response's body size.
curl -s -I "$1" | awk '/Content-Length/ {print $2}'
