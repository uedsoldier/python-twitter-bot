#!/bin/bash

echo "Container entrypoint"
printenv > /etc/environment
cron -f