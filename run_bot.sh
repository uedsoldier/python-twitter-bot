#!/bin/bash

# This script is executed from the container's root folder: /app

# Change to script source directory
cd /Twitter-bot/python-twitter-bot/ || exit 1

# Log start with timestamp
echo "[$(date)] Starting bot execution..."

# Run the Python script with the full path
# The script path is src/main.py, since we are in the root directory.
/usr/local/bin/python src/main.py

# Log completion
echo "[$(date)] Bot execution completed"