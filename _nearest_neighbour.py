from PIL import Image, ImageFile
import numpy as np
import math, cv2

ImageFile.LOAD_TRUNCATED_IMAGES = True

def nearest_neighbor_interpolation(image, scale_factor):
    # Get the dimensions of the input image
    input_width, input_height = image.size

    # Calculate the output dimensions
    output_height = int(input_height * scale_factor)
    output_width = int(input_width * scale_factor)

    # Create an empty array for the output image
    output_image = np.zeros((output_height, output_width), dtype=np.uint8)

    # Iterate over each pixel in the output image
    for y in range(output_height):
        for x in range(output_width):
            # Calculate the corresponding pixel coordinates in the input image
            input_x = int(x / scale_factor)
            input_y = int(y / scale_factor)

            # Get the pixel value from the input image
            pixel_value = image.getpixel((input_x, input_y))

            # Set the pixel value in the output image
            output_image[y, x] = pixel_value

    # Create a PIL image from the output array
    output_image = Image.fromarray(output_image)

    return output_image
