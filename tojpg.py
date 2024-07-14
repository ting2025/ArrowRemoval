import os
from PIL import Image

folder_path = "data/masks"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # Open the image
        img = Image.open(os.path.join(folder_path, filename))

        # Convert and save as .png
        new_filename = filename.replace(".jpg", ".png")
        img.save(os.path.join(folder_path, new_filename), "PNG")

        # Delete the .jpg file
        os.remove(os.path.join(folder_path, filename))