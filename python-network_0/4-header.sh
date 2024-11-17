#!/bin/bash
# Script to send a GET request to URL and display the body of the response with a custom header
curl -sH "X-School-User-Id: 98" "$1"
