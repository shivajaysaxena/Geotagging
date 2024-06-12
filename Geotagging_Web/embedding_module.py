# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:36:31 2024

@author: shivajay
"""

from PIL import Image
import hashlib

# Function to read pixel values of an image and store them in a file
def read_pixel_values(image_path, output_file):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    with open(output_file, 'w') as f:
        for i, pixel in enumerate(pixels):
            f.write(f"Pixel {i}: {','.join(map(str, pixel))}\n")
    return len(pixels)

# Function to embed text into an image
def embed_text(image_path, text, output_file):
    img = Image.open(image_path)
    width, height = img.size
    message = text.encode('utf-8')
    length = len(message)
    hash_value = hashlib.sha256(message).hexdigest()

    # Original pixels
    original_pixels = list(img.getdata())

    # Embed length of message
    img.putpixel((0, 0), (length,))

    # Embed message
    for i in range(length):
        img.putpixel(((i+1) % width, (i+1) // width), (message[i],))

    # Embed hash value
    for i in range(len(hash_value)):
        img.putpixel(((length + 1 + i) % width, (length + 1 + i) // width), (ord(hash_value[i]),))

    img.save(output_file)

    # Updated pixels after embedding
    updated_pixels = list(img.getdata())

    # Write updated pixel values to a file
    with open('output1.txt', 'w') as f:
        for i, (old, new) in enumerate(zip(original_pixels, updated_pixels)):
            if old != new:
                f.write(f"Pixel {i}: {','.join(map(str, new))}\n")

    # Count the number of updated pixels
    num_updated_pixels = sum(1 for old, new in zip(original_pixels, updated_pixels) if old != new)

    # Print number of pixels in the image and number of updated pixels
    print("Number of Pixels in the Image:", len(original_pixels))
    print("Number of Updated Pixels after Embedding:", num_updated_pixels)

# Main function
if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    original_pixel_count = read_pixel_values(image_path, 'output.txt')
    
    text_to_embed = input("Enter the text to embed: ")
    print("the lenght of the string: ", len(text_to_embed))
    print("the binary lenght of the string: ", 8*len(text_to_embed))
    embed_text(image_path, text_to_embed, 'input_embed.png')


