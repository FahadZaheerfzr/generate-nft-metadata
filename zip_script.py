

# Create a zip file with all the metadata and images

import zipfile
import os

# Create a zip file
with zipfile.ZipFile("RobuSnipeNFT.zip", "w") as file:
  # Add all the metadata files
  for i in range(1, 5009):
    file.write(f"{i}.json")
  # Add all the image files
  for i in range(1, 5008):
    file.write(f"{i}.png")