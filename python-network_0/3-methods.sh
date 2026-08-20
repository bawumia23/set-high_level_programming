#!/bin/bash
# displays all HTTP methods a server accepts for a given URL
curl -s -X OPTIONS -i "$1" | grep -i '^Allow:' | sed 's/[Aa]llow: //' | tr -d '\r'
