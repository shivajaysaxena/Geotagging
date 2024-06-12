# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:25:07 2024

@author: shivajay
"""

# from PIL import Image whole cpy1
# import hashlib

# # # Function to read the encoded image and extract the message original
# # def read_encoded_image(image_path):
# #     img = Image.open(image_path)
# #     width, height = img.size

# #     # Extract length of the message
# #     length = img.getpixel((0, 0))[0]  # Unpack the tuple and get the first element

# #     # Extract message
# #     message = []
# #     for i in range(1, length + 1):
# #         pixel_value = img.getpixel((i % width, i // width))
# #         message.append(chr(pixel_value[0]))  # Extract the first channel value (assuming grayscale)

# #     # Extract hash value
# #     hash_start_index = length + 1
# #     hash_value = ""
# #     for i in range(hash_start_index, hash_start_index + 64):
# #         pixel_value = img.getpixel((i % width, i // width))
# #         hash_value += chr(pixel_value[0])  # Extract the first channel value (assuming grayscale)

# #     return ''.join(message), hash_value

# # # Function to read the encoded image and extract the message cpy1
# # def read_encoded_image(image_path):
# #     img = Image.open(image_path)
# #     width, height = img.size

# #     # Extract length of the message
# #     length = img.getpixel((0, 0))[0]  # Unpack the tuple and get the first element

# #     # Check if the expected length exceeds the number of pixels in the image
# #     expected_length = (width * height) - 65  # Subtracting 65 for the metadata (length + hash)
# #     if length > expected_length:
# #         raise ValueError("Image has been altered or cropped.")

# #     # Extract message
# #     message = []
# #     for i in range(1, length + 1):
# #         pixel_value = img.getpixel((i % width, i // width))
# #         message.append(chr(pixel_value[0]))  # Extract the first channel value (assuming grayscale)

# #     # Extract hash value
# #     hash_start_index = length + 1
# #     hash_value = ""
# #     for i in range(hash_start_index, hash_start_index + 64):
# #         pixel_value = img.getpixel((i % width, i // width))
# #         hash_value += chr(pixel_value[0])  # Extract the first channel value (assuming grayscale)

# #     return ''.join(message), hash_value




# # Function to compare hash values
# def compare_hashes(message, original_hash):
#     computed_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
#     return computed_hash == original_hash

# # Main function
# if __name__ == "__main__":
#     encoded_image_path = input("Enter the path to the encoded image: ")
    
#     # Read the encoded image
#     encoded_message, original_hash = read_encoded_image(encoded_image_path)
    
#     # Compare the computed hash with the original hash
#     if compare_hashes(encoded_message, original_hash):
#         print("Image has not been altered.")
#         print("Encoded Message:", encoded_message)
#     else:
#         print("Image has been altered.")






# #CORRECT
# from PIL import Image
# import hashlib

# # Function to read the encoded image and extract the message
# def read_encoded_image(image_path):
#     img = Image.open(image_path)
#     width, height = img.size

#     # Extract length of the message
#     length = img.getpixel((0, 0))[0]  # Unpack the tuple and get the first element

#     # Check if the expected length exceeds the number of pixels in the image
#     expected_length = (width * height) - 65  # Subtracting 65 for the metadata (length + hash)
#     if length > expected_length:
#         raise ValueError("Image has been altered or cropped.")

#     # Extract message
#     message = []
#     for i in range(1, length + 1):
#         pixel_value = img.getpixel((i % width, i // width))
#         message.append(chr(pixel_value[0]))  # Extract the first channel value (assuming grayscale)

#     # Extract hash value
#     hash_start_index = length + 1
#     hash_value = ""
#     for i in range(hash_start_index, hash_start_index + 64):
#         pixel_value = img.getpixel((i % width, i // width))
#         hash_value += chr(pixel_value[0])  # Extract the first channel value (assuming grayscale)

#     return ''.join(message), hash_value

# # Function to compare hash values
# def compare_hashes(message, original_hash):
#     computed_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
#     return computed_hash == original_hash

# # Main function
# if __name__ == "__main__":
#     encoded_image_path = input("Enter the path to the encoded image: ")
    
#     try:
#         # Read the encoded image
#         encoded_message, original_hash = read_encoded_image(encoded_image_path)
        
#         # Compare the computed hash with the original hash
#         if compare_hashes(encoded_message, original_hash):
#             print("Image has not been altered.")
#             print("Encoded Message:", encoded_message)
#         else:
#             print("Image has been altered.")
#     except ValueError as e:
#         print("Error:", e)




# extraction_module.py

from PIL import Image
import hashlib

def extract_data(image_file):
    # Function to read the encoded image and extract the message
    def read_encoded_image(img):
        width, height = img.size

        # Extract length of the message
        length = img.getpixel((0, 0))[0]  # Unpack the tuple and get the first element

        # Check if the expected length exceeds the number of pixels in the image
        expected_length = (width * height) - 65  # Subtracting 65 for the metadata (length + hash)
        if length > expected_length:
            raise ValueError("Image has been altered or cropped.")

        # Extract message
        message = []
        for i in range(1, length + 1):
            pixel_value = img.getpixel((i % width, i // width))
            message.append(chr(pixel_value[0]))  # Extract the first channel value (assuming grayscale)

        # Extract hash value
        hash_start_index = length + 1
        hash_value = ""
        for i in range(hash_start_index, hash_start_index + 64):
            pixel_value = img.getpixel((i % width, i // width))
            hash_value += chr(pixel_value[0])  # Extract the first channel value (assuming grayscale)

        return ''.join(message), hash_value

    # Function to compare hash values
    def compare_hashes(message, original_hash):
        computed_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
        return computed_hash == original_hash

    try:
        img = Image.open(image_file)
        encoded_message, original_hash = read_encoded_image(img)

        if compare_hashes(encoded_message, original_hash):
            return encoded_message
        else:
            return "Image has been altered."
    except ValueError as e:
        return str(e)

