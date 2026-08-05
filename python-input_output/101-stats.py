#!/usr/bin/python3
"""Module to parse logs and compute metrics."""
import sys


def print_stats(total_size, status_codes):
    """Prints the computed statistics.

    Args:
        total_size: The total file size.
        status_codes: A dictionary of status code counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 2:
            try:
                status = int(parts[-2])
                size = int(parts[-1])
                if status in status_codes:
                    status_codes[status] += 1
                total_size += size
            except (ValueError, IndexError):
                pass
        count += 1
        if count % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
