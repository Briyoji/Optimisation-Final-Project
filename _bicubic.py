from PIL import Image, ImageFile
import numpy as np
import math, cv2

ImageFile.LOAD_TRUNCATED_IMAGES = True

def cubicConv(x, a):
    if abs(x) < 1:
        return (a + 2) * abs(x)**3 - (a + 3) * abs(x)**2 + 1
    elif abs(x) < 2:
        return a * abs(x)**3 - 5 * a * abs(x)**2 + 8 * a * abs(x) - 4 * a
    else:
        return 0

def getPixel(image, x, y):
    if x < 0 or y < 0 or x >= len(image[0]) or y >= len(image):
        return 0
    return image[y][x]

def bicubic_interpolation(image, scale_factor, a=-0.5):

    image = np.array(image)
    input_height, input_width = image.shape
    
    output_height = int(input_height * scale_factor)
    output_width = int(input_width * scale_factor)

    result = np.zeros((output_height, output_width), dtype=np.uint8)

    for y in range(output_height):
        for x in range(output_width):


            srcX = (x / output_width) * input_width
            srcY = (y / output_height) * input_height

            topLeftX = math.floor(srcX) - 1
            topLeftY = math.floor(srcY) - 1

            neighbors = []
            for i in range(4):
                for j in range(4):
                    neiX = topLeftX + i
                    neiY = topLeftY + j
                    neighbors.append((neiX, neiY))

            fracX = srcX - math.floor(srcX)
            fracY = srcY - math.floor(srcY)

            distances = []
            for neighbor in neighbors:
                distX = abs(neighbor[0] - (topLeftX + fracX))
                distY = abs(neighbor[1] - (topLeftY + fracY))
                distances.append((distX, distY))

            weights = []
            for distance in distances:
                weightX = cubicConv(distance[0], a)
                weightY = cubicConv(distance[1], a)
                weight = weightX * weightY
                weights.append(weight)

            interpolated = 0
            for i in range(len(neighbors)):
                pixel = getPixel(image, neighbors[i][0], neighbors[i][1])
                weight = weights[i]
                interpolated += pixel * weight

            interpolated = max(0, min(interpolated, 255))
            result[y, x] = interpolated

    # resultArray = np.array(result)
    # unblurred = Image.fromarray(resultArray)
    barray = cv2.GaussianBlur(result, (15, 15), 0)
    UpdatedImage = Image.fromarray(barray)
    return UpdatedImage