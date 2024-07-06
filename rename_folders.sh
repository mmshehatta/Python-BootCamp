#!/bin/bash

# Define the prefix to add (0)
prefix="0"

# Get the current directory (replace with your actual folder path if needed)
current_dir=$(pwd)

# Loop through all files and folders in the current directory
for file in *; do
  # Check if it's a directory (skip non-directories)
  if [[ -d "$current_dir/$file" ]]; then
    # Check if the name starts with "week_"
    if [[ "$file" == week_* ]]; then
      # Extract the week number (remove "week_")
      week_number=${file#week_}
      
      # Construct the new name with leading zero
      new_name="$prefix$week_number""_week_$week_number"
      
      # Rename the folder
      mv "$current_dir/$file" "$current_dir/$new_name"
      echo "Renamed '$file' to '$new_name'"
    fi
  fi
done

echo "Renaming completed!"
