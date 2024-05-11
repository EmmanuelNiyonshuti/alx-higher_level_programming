#!/bin/bash
#sends a JSON POST request to a url and displays the body of a response
curl -s -X POST -d "@$2" "$1"