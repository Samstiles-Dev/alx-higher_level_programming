#!/bin/bash
# Sends a GET request to given URL with a header variable.
curl -sH "X-School-User-Id: 98" "$1"
