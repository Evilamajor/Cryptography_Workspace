#!/bin/bash

# Navigate to the workspace (adjust if needed)
cd "$(dirname "$0")"

# Add all changes
git add .

# Commit with a descriptive message (date/time stamp)
git commit -m "Auto-update: $(date +'%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push origin main


