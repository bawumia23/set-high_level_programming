#!/bin/bash
# sends a PUT request with a user_id param and Origin header to catch_me
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
