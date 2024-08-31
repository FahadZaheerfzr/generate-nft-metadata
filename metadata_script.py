
# Create a json file with metadata for the dataset
import json

i = 0

metadata = {
  "name": "RobuSnipeNFT",
  "description": "Robusnipe NFTs grant premium access to the Robusnipe platform, unlocking advanced features and exclusive perks. These NFTs offer VIP access to the Robusnipe ecosystem, and perks that will enhance your trading experience.",
}

for i in range(1, 5008):
  with open(f"{i}.json", "w") as file:
    metadata["image"] = f"https://ipfs.arbornft.io/robusnipe/{i-1}.png"
    json.dump(metadata, file)