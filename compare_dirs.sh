#!/bin/bash

read -p "Enter the first directory path: " dir1
read -p "Enter the second directory path: " dir2

if [[ ! -d "$dir1" || ! -d "$dir2" ]]; then
    echo "Error: One or both paths are not valid directories."
    exit 1
fi

# List only subdirectories (top level, no recursion)
subdirs1=$(find "$dir1" -mindepth 1 -maxdepth 1 -type d -printf "%f\n" | sort)
subdirs2=$(find "$dir2" -mindepth 1 -maxdepth 1 -type d -printf "%f\n" | sort)

echo "Comparing folder names..."

diff <(echo "$subdirs1") <(echo "$subdirs2")
