# CONVERT ANY VIDEO FILE TO MP3 AUDIO

import os
from moviepy.editor import *

file_path = input("Enter absolute file path: ")

print(f"Converting file at path {file_path}")
print(os.path.exists(file_path))

if os.path.exists(file_path):
	video = VideoFileClip(file_path)
	file_name = input("Enter file name: ")

	print(f"Converting file to {file_name}")

	video.audio.write_audiofile(file_name + ".mp3")

else:
	print("ERROR in file") 

# Download python from => https://www.python.org/
# Install moviepy => pip install moviepy

# Run python ./[file_name].py

# Kinyua Nyaga 😉 