from PIL import Image, ImageFile
import numpy as np
import threading
import tkthread

from utils import *

# Setting Attribute
ImageFile.LOAD_TRUNCATED_IMAGES = True

class Interpolater :
    def __init__(self, interpolation_type : int = 0, file_path : str = "", scaling_factor : float = 1.0, demo_mode : bool = False) -> None:
        self.interpolation_type = interpolation_type
        self.file_path = file_path
        self.scale_factor = scaling_factor if scaling_factor else 1

        self.interpolation_name = None
        self.scaled_down = None
        self.updated_image = None
        self.original = None

        interpolation_map = {
            0 : self.nearest_neighbour,
            1 : self.bilinear,
            2 : self.bicubic,
            3 : self.lanczos
        }

        try:
            self.original = Image.open(self.file_path)
            self.original = self.original.convert('L')
            
            temp = self.original.copy() 

            # tkinter_thread = threading.Thread(target=display_image_with_title, args=(temp, "Original Image"))
            # tkinter_thread.start()

            # tkthread.call_nosync(display_image_with_title, temp, "Original Image")
            display_image_with_title(temp, "Originl Image", 1)

            self.scale_down()
            self.original = np.array(self.original)

            if not demo_mode : 
                interpolation_map[self.interpolation_type]()
                display_image_with_title(self.updated_image, "Interpolated Image", 1)

            else :
                images = [self.original]
                titles = ["Original", "Nearest Neighbour", "Bilinear", "Bicubic", "Lanczos"]
                # titles = ["Original", "Nearest Neighbour", "Bilinear", "Bicubic"]

                for method in range(len(titles)-1   ) :
                    interpolation_map[method]()
                    images.append(self.updated_image.copy())
                    print(f"Completed {titles[method+1].capitalize()} Interpolation")

                display_demo_with_titles(images, titles)
            # tkthread.call_nosync(display_image_with_title, self.updated_image, "Interpolated Image", 1)
            # tkinter_thread = threading.Thread(target=display_image_with_title, args=(self.updated_image, "Interpolated Image", 1))
            # tkinter_thread.start()

        except IOError:
            raise IOError


    def scale_down(self):
        # Calculate the input dimensions
        print(type(self.original))
        input_width, input_height = self.original.size

        # Calculate the output dimensions
        output_width = int(input_width / self.scale_factor)
        output_height = int(input_height / self.scale_factor)

        # Resize the image using the calculated dimensions
        self.scaled_down = self.original.resize((output_width, output_height), Image.ADAPTIVE)

        self.scaled_down = np.array(self.scaled_down)
        self.scaled_down = Image.fromarray(self.scaled_down)

    def nearest_neighbour(self) :
        self.interpolation_name = 'nearest_neighbour'
        self.updated_image = nearest_neighbor_interpolation(self.scaled_down, self.scale_factor)
        pass
    
    def bilinear(self) :
        self.interpolation_name = 'bilinear'
        self.updated_image = bilinear_interpolation(self.scaled_down, self.scale_factor)
        pass
    
    def bicubic(self) :
        self.interpolation_name = 'bicubic'
        self.updated_image = bicubic_interpolation(self.scaled_down, self.scale_factor)
        pass
    
    def lanczos(self) :
        self.interpolation_name = 'lanczos'
        self.updated_image = lanczos_interpolation(self.scaled_down, self.scale_factor)
        pass

    

def interpolate_image(interpolation_type : int = 0, file_path : str = "", scale_factor : float = 1, demo_mode : bool = False) -> None :
    interpolator = Interpolater(interpolation_type, file_path, scale_factor, demo_mode)