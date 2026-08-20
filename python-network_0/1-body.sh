#!/bin/bash
# sends a GET request, follows redirects, and displays the body if status is 200
[ "$(curl -s -L -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s -L "$1"
