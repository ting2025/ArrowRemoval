import os
from PIL import Image

# Set the directory containing the images
directory = "data/imgs"

# Loop through each image in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)

        # Convert the image to RGB mode (removes the infrared channel)
        image = image.convert("RGB")
        if image.mode == 'RGBA':
            continue
        print(image_path)
        # Save the image
        image.save(image_path)