'''
	Course   : OPTIMISATION 
	Code     : FM216
	Semester : 03
'''

#  Importing Necessary Modules
from questionaire import get_config
from apply_interpolation import interpolate_image

interpolation_type, file_path, scaling_factor = get_config()

print(interpolation_type, file_path, scaling_factor)

interpolate_image(interpolation_type, file_path, scaling_factor, True)