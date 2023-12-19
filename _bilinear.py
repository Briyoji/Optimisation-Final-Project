from PIL import Image, ImageFile
import numpy as np
import math, cv2

ImageFile.LOAD_TRUNCATED_IMAGES = True

def bilinear_interpolation(image, scale_factor):
    # Get the dimensions of the input image
    input_width, input_height = image.size

    # Calculate the output dimensions
    output_width = int(input_width * scale_factor)
    output_height = int(input_height * scale_factor)

    # Create an empty array for the output image
    output_image = np.zeros((output_height, output_width), dtype=np.uint8)

    # Iterate over each pixel in the output image
    for y in range(output_height):
        for x in range(output_width):
            # Calculate the corresponding pixel coordinates in the input image
            input_x = x / scale_factor
            input_y = y / scale_factor

            # Calculate the indices of the neighboring pixels
            x1 = int(input_x)
            y1 = int(input_y)
            x2 = x1 + 1
            y2 = y1 + 1

            # Clip the indices to the valid range
            x1 = max(0, min(x1, input_width - 1))
            y1 = max(0, min(y1, input_height - 1))
            x2 = max(0, min(x2, input_width - 1))
            y2 = max(0, min(y2, input_height - 1))

            # Calculate the weights for interpolation
            weight_x = input_x - x1
            weight_y = input_y - y1

            # Perform bilinear interpolation
            interpolated_value = (1 - weight_x) * (1 - weight_y) * image.getpixel((x1, y1)) + \
                                 weight_x * (1 - weight_y) * image.getpixel((x2, y1)) + \
                                 (1 - weight_x) * weight_y * image.getpixel((x1, y2)) + \
                                 weight_x * weight_y * image.getpixel((x2, y2))

            # Set the pixel value in the output image
            output_image[y, x] = int(interpolated_value)

    # Create a PIL image from the output array
    output_image = Image.fromarray(output_image)

    return output_image