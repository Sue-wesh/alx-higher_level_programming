#!/bin/bash
#sends JSON POST request to URL passed as 1st arg, display body of respons
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
