#!/bin/bash

# Find all .json files in the current directory
# and its subdirectories, then filter out those
# that don't contain '_cu_nf' in their filename
# and delete them.

find ./ -type f -name "*.json" | grep -v "_cu_nf" | while IFS= read -r file; do
    rm "$file"
done

echo "All .json files not containing '_cu_nf' in their filename have been removed."
