# mp3_organizer.py

import os
import shutil

# 1. Define where to start and where to end
# ~ is a shortcut for your Mac Home folder (e.g., /Users/yourname)
search_root = os.path.expanduser("~/Downloads") 
destination = os.path.expanduser("~/Documents/Audio")

# 2. Common Mac audio extensions
audio_exts = (".mp3", ".wav", ".m4a", ".flac", ".aiff", ".aac")

print(f"Deep-scanning {search_root} for audio files...")

# 3. Use os.walk to go through every single sub-folder
for root, dirs, files in os.walk(search_root):
    for filename in files:
        if filename.lower().endswith(audio_exts):
            # Construct the full path of where the file is currently sitting
            current_file_path = os.path.join(root, filename)
            
            # Construct where it's going
            target_file_path = os.path.join(destination, filename)
            
            # Move it!
            try:
                shutil.move(current_file_path, target_file_path)
                print(f"Moved: {filename}")
            except Exception as e:
                print(f"Could not move {filename}: {e}")

print("\nAll done! Your audio files are consolidated.")