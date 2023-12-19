from PIL import Image, ImageFile
import numpy as np
import math, cv2

ImageFile.LOAD_TRUNCATED_IMAGES = True

def lanczos_interpolation(image, scale_factor):
    # Get the dimensions of the input image
    input_width, input_height = image.size

    # Calculate the output dimensions
    output_width = int(input_width * scale_factor)
    output_height = int(input_height * scale_factor)

    # Create an empty array for the output image
    output_image = np.zeros((output_height, output_width), dtype=np.uint8)

    # Define the Lanczos kernel function
    def lanczos_kernel(x):
        if x == 0:
            return 1.0
        elif -1 <= x <= 1:
            return np.sin(np.pi * x) * np.sin(np.pi * x / scale_factor) / (np.pi * np.pi * x * x)
        else:
            return 0.0

    # Iterate over each pixel in the output image
    for y in range(output_height):
        for x in range(output_width):
            # Calculate the corresponding pixel coordinates in the input image
            input_x = x / scale_factor
            input_y = y / scale_factor

            # Calculate the indices of the neighboring pixels
            x1 = int(input_x) - 2
            y1 = int(input_y) - 2
            x2 = x1 + 4
            y2 = y1 + 4

            # Clip the indices to the valid range
            x1 = max(0, min(x1, input_width - 1))
            y1 = max(0, min(y1, input_height - 1))
            x2 = max(0, min(x2, input_width - 1))
            y2 = max(0, min(y2, input_height - 1))

            # Calculate the interpolated pixel value
            interpolated_value = 0.0
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    weight_x = lanczos_kernel((input_x - i) / scale_factor)
                    weight_y = lanczos_kernel((input_y - j) / scale_factor)
                    interpolated_value += weight_x * weight_y * image.getpixel((i, j))

            # Set the pixel value in the output image
            output_image[y, x] = int(interpolated_value)

    # Create a PIL image from the output array
    output_image = Image.fromarray(output_image)

    return output_image
