#!/bin/bash
# displays only the status code of the response from a given URL
curl -s -o /dev/null -w "%{http_code}" "$1"
