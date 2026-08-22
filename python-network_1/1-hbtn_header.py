#!/usr/bin/python3
"""Module that displays the X-Request-Id header for a given URL."""
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
