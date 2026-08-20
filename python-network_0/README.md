# python-network_0

## Description

This project covers the basics of the HTTP protocol using `curl` in Bash
scripts, plus one algorithm task (finding a peak in an unsorted list of
integers) written in Python.

All Bash scripts in this project are exactly 3 lines long, start with
`#!/bin/bash`, have a comment on the second line explaining what they do,
and use `curl -s` (silent mode) for every request. They were written and
tested against the sandbox web server running on port 5000
(`0.0.0.0:5000`).

## Tasks

| File | Description |
| --- | --- |
| `0-body_size.sh` | Displays the size (in bytes) of the body of the response to a URL. |
| `1-body.sh` | Sends a GET request and displays the body only when the response status is 200. |
| `2-delete.sh` | Sends a DELETE request to a URL and displays the body of the response. |
| `3-methods.sh` | Displays all HTTP methods a server accepts for a given URL. |
| `4-header.sh` | Sends a GET request with the header `X-School-User-Id: 98` and displays the body. |
| `5-post_params.sh` | Sends a POST request with `email` and `subject` parameters and displays the body. |
| `6-peak.py` / `6-peak.txt` | `find_peak` finds a peak value in a list of unsorted integers using a binary-search approach; `6-peak.txt` states the algorithm's complexity. |
| `100-status_code.sh` | Displays only the status code of the response to a URL, without using any pipe, redirection, `;`, or `&&`. |
| `101-post_json.sh` | Sends a POST request whose body is the JSON content of a file, and displays the response body. |
| `102-catch_me.sh` | Sends a request to `/catch_me` that makes the server respond with `You got me!`. |

## Usage

```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
./2-delete.sh 0.0.0.0:5000/route_3
./3-methods.sh 0.0.0.0:5000/route_4
./4-header.sh 0.0.0.0:5000/route_5
./5-post_params.sh 0.0.0.0:5000/route_6
./100-status_code.sh 0.0.0.0:5000
./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
./102-catch_me.sh
./6-main.py
```

## Author

Tajudeen - ALX Software Engineering Program
