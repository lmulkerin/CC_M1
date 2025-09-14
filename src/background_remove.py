'''This file is used to remove the backgrounds of images'''

import rembg # Used to remove backgrounds - depends on onnxruntime which I installed with 'pip install onnxruntime'
import numpy as np
from PIL import Image

def remove_background(img):
    '''
    Uses rembg package to remove the background of an image

    Args:
        img (str): path to desired image

    Returns:    
        Image object with background removed.
    '''
    image = Image.open(img)
    image_arr = np.array(image)
    output_arr = rembg.remove(image_arr)
    output_img = Image.fromarray(output_arr)
    return output_img