#!/bin/bash
#sends a GET request to the url and displays the body of the response
curl -s -G -H "X-School-User-Id=98" "$1"
