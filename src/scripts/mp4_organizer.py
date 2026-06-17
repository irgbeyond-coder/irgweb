# mp4_organizer.py

import os
import shutil

# 1. Setup the paths (Change 'yourname' to your Mac username)
source_dir = os.path.expanduser("~/Downloads") 
destination_dir = os.path.expanduser("~/Documents/Video")

# 2. Define what counts as a "movie"
movie_extensions = (".mp4", ".mov", ".mkv", ".avi")

print(f"Searching for movies in {source_dir}...")

# 3. The Logic Loop
for filename in os.listdir(source_dir):
    if filename.lower().endswith(movie_extensions):
        # Create the full path for the file
        old_path = os.path.join(source_dir, filename)
        new_path = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.move(old_path, new_path)
        print(f"Successfully moved: {filename}")

print("Cleanup complete!")