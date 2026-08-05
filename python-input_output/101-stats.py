#!/usr/bin/python3
"""Log parsing module."""

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in status_codes:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) >= 2:
            status = parts[-2]
            if status in counts:
                counts[status] += 1
            try:
                total_size += int(parts[-1])
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
