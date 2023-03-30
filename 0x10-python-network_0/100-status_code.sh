#!/bin/bash
#send request to URL passed as arg, display only status code of response.
curl -so /dev/null -w "%{http_code}" "$1"
