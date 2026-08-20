#!/bin/bash
# sends a POST request with a JSON file's content and displays the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
