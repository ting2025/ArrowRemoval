from PIL import Image
import os

# Path to the directory containing the images
directory = 'data/masks'

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Open the image
        image = Image.open(os.path.join(directory, filename))

        # Create a new white canvas image of size 500x500 pixels
        new_image = Image.new('RGB', (500, 500), (0, 0, 0))

        # Calculate the position to paste the original image on the canvas
        paste_position = ((500 - image.width) // 2, (500 - image.height) // 2)

        # Paste the original image onto the canvas
        new_image.paste(image, paste_position)

        # Save the new image with the same filename
        new_image.save(os.path.join(directory, filename))