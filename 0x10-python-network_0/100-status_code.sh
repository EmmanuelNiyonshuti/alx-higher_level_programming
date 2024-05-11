#!/bin/bash
#sends a request to a url and displays only the status code
curl -s -w "%{http_code}" -o /dev/null "$1"