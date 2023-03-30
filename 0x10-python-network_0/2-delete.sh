#!/bin/bash
# send DELETE request to URL passed as 1st arg and display body of response
curl -sX DELETE "$1"
