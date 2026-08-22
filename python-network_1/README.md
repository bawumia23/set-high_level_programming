# python-network_1

## Description

This project continues the HTTP fundamentals from `python-network_0`, but
moves the work from Bash/`curl` into Python, using two different libraries:

- **`urllib`** (Python's built-in HTTP client) for tasks 0-3
- **`requests`** (the popular third-party HTTP client) for tasks 4-10

Both approaches accomplish the same goals — sending requests, reading
headers, posting data, and handling errors — so the project doubles as a
comparison between the low-level standard-library way and the higher-level,
more ergonomic third-party way of doing HTTP in Python.

## Tasks

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches the ALX intranet status page with `urllib` and prints the response body's type, raw bytes, and UTF-8 decoded content. |
| `1-hbtn_header.py` | Fetches a URL with `urllib` and prints the `X-Request-Id` response header. |
| `2-post_email.py` | Sends a POST request with an `email` parameter using `urllib` and prints the response body. |
| `3-error_code.py` | Fetches a URL with `urllib`, printing the body on success or `Error code: <code>` if an `HTTPError` is raised. |
| `4-hbtn_status.py` | Same as task 0 but using `requests`. |
| `5-hbtn_header.py` | Same as task 1 but using `requests`. |
| `6-post_email.py` | Same as task 2 but using `requests`. |
| `7-error_code.py` | Same as task 3, but checks `response.status_code >= 400` instead of catching an exception. |
| `8-json_api.py` | POSTs a search letter to `/search_user` and parses the JSON response, printing `[<id>] <name>`, `No result`, or `Not a valid JSON`. |
| `10-my_github.py` | Uses HTTP Basic Authentication (a GitHub username + personal access token) to fetch and print the authenticated user's numeric GitHub id. |
| `100-github_commits.py` | Uses the GitHub API to list the 10 most recent commits of a given repository, printing `<sha>: <author name>` per line. |

## Usage

```
./0-hbtn_status.py
./1-hbtn_header.py https://alx-intranet.hbtn.io
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./3-error_code.py http://0.0.0.0:5000/status_401
./4-hbtn_status.py
./5-hbtn_header.py https://alx-intranet.hbtn.io
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./7-error_code.py http://0.0.0.0:5000/status_500
./8-json_api.py a
./10-my_github.py <username> <personal-access-token>
./100-github_commits.py rails rails
```

## Author

Tajudeen - ALX Software Engineering Program
