#!/bin/bash
# diplay all HTTP methods the server will accept
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
