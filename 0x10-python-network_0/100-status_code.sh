#!/bin/bash
# diplay all HTTP methods the server will accept
curl -so /dev/null -w "%{http_code}" "$1"
