#!/usr/bin/python3
"""Module that sends a POST request with an email parameter via urllib."""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
