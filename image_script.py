import os

# Read all the folders in the current directory

i = 0

for folder in os.listdir():
  if os.path.isdir(folder):
    # Read all the files in the folder
    for file in os.listdir(folder):
      # Rename the file
      os.rename(f"{folder}/{file}", f"{i}.png")
      i+=1