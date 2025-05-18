#!/bin/bash

# Navigate to workspace
cd "$(dirname "$0")"

# Activate the virtual environment
source cryptography_env/bin/activate

# Add, commit, and push changes
git add .
COMMIT_MESSAGE="Auto-update: $(date +'%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MESSAGE"
git push origin main

# Run ChatGPT script
CHATGPT_COMMENT=$(python3 chatgpt_operator.py "$COMMIT_MESSAGE")

# Log ChatGPT comment
echo "$(date +'%Y-%m-%d %H:%M:%S') - $CHATGPT_COMMENT" >> chatgpt_commit_comments.log
echo "ChatGPT Comment: $CHATGPT_COMMENT"

# Deactivate environment after running
deactivate

