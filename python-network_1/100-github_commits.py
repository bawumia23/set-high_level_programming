#!/usr/bin/python3
"""Module that lists the 10 most recent commits of a GitHub repository."""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit', {}).get('author', {}).get('name')
        print("{}: {}".format(sha, author))
