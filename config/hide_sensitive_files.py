import os
import shutil

# --- Documentation ---
# This script performs preprocessing on the documentation source
# before MkDocs builds the documentation website.
#
# Functionality:
# - Excludes (deletes) directories from the documentation source 
#   based on a specified prefix (default: '~').
#
# Environment Variables:
# - DOCS_PATH: Specify the path to the documentation source. Default is './wiki'.
# - EXCLUDE_PREFIX: Specify the prefix of directories to exclude. Default is '~'.

# --- Configuration ---
# Fetch environment variables with default values as fallbacks
DOCS_PATH = os.getenv('DOCS_PATH', './wiki')
EXCLUDE_PREFIX = os.getenv('EXCLUDE_PREFIX', '~')

# --- Core Logic ---
# Iterate through all items in the docs directory
for item in os.listdir(DOCS_PATH):
    item_path = os.path.join(DOCS_PATH, item)
    # Check if the item is a directory and starts with the exclude prefix
    if os.path.isdir(item_path) and item.startswith(EXCLUDE_PREFIX):
        # Remove the directory
        shutil.rmtree(item_path)
        print(f"Excluded: {item_path}")

# --- Notes ---
# - Ensure to validate the impact in a safe environment before using in production.
# - Removed directories are not recoverable unless backed up previously.
