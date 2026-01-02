#!/bin/bash

read -p "Enter the directory path: " dir
read -p "Enter the number of most recent files to show: " n

if [[ ! -d "$dir" ]]; then
    echo "Error: '$dir' is not a valid directory."
    exit 1
fi

if ! [[ "$n" =~ ^[0-9]+$ ]]; then
    echo "Error: '$n' is not a valid integer."
    exit 1
fi

echo "🔎 Showing the $n most recently modified files in '$dir' (including subdirectories):"
find "$dir" -type f -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -n "$n" | awk '{ $1=""; print substr($0,2) }'
