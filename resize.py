from PIL import Image
import os

# Set the path to the folder containing the images
folder_path = "data/imgs"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".png"):
        # Open the image file
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Determine the size of the new square image
        width, height = image.size
        size = min(width, height)

        # Resize the image
        resized_image = image.resize((size, size))
        
        colors_to_keep = [(0,0,0), (102,255,102)]
        count=0
        for x in range( resized_image.width):
            for y in range( resized_image.height):
                # get the color of the current pixel
                pixel_color =  resized_image.getpixel((x,y))
                # check if the color is not in the list of colors to keep
                if pixel_color not in colors_to_keep:
                    # if it's not, change the color to (0,0,0)
                    resized_image.putpixel((x,y), (0,))

        # Save the new image
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_image_path = os.path.join(folder_path, new_filename)
        resized_image.save(new_image_path)

folder_path = "data/masks"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".png"):
        # Open the image file
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Determine the size of the new square image
        width, height = image.size
        size = min(width, height)

        # Resize the image
        resized_image = image.resize((size, size))
        colors_to_keep = [(0,0,0), (102,255,102)]
        count=0
        for x in range( resized_image.width):
            for y in range( resized_image.height):
                # get the color of the current pixel
                pixel_color =  resized_image.getpixel((x,y))
                # check if the color is not in the list of colors to keep
                if pixel_color not in colors_to_keep:
                    # if it's not, change the color to (0,0,0)
                    resized_image.putpixel((x,y), (0,))

        # Save the new image
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_image_path = os.path.join(folder_path, new_filename)
        resized_image.save(new_image_path)