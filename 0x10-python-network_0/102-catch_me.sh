#!/bin/bash
# server to respond witha message
curl -sL -X PUT "0.0.0.0:5000/catch_me" -H "Origin: You got me!" -d "user_id=98"
