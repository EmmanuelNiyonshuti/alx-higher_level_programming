#!/usr/bin/python3
"""
makes a GET request to the GitHub API's /user endpoint,
retrieves information about the authenticated user.
using Basic Authentication with GitHub username and personal access token (PAT)
to authenticate the request.
retrieves the response from the API, parses it as JSON,
and then prints the user ID if the request is successful.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    r_dict = r.json()
    print(r_dict.get('id'))
