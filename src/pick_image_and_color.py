import os
import numpy as np

'''This chooses an image and a color based on transition matrices, then returns them as a tuple'''

# This was needed to access images properly:
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from src/
IMAGE_DIR = os.path.join(BASE_DIR, "images")


def map_images():
    '''Maps image names to image paths

    Args: None

    Returns:
        A dictionary mapping image numbers to their paths
    '''
    image_map = {}
    for file in os.listdir(IMAGE_DIR):
        name, ext = os.path.splitext(file)
        if name.isdigit():
            image_map[str(name)] = os.path.join(IMAGE_DIR, file)
    return image_map


class ImageAndColorChooser:
    '''Allows us to choose an image and color based off of transition matrices '''
    def __init__(self, image_matrix, color_matrix):
        '''An initializer

        Args:
            image_matrix (dict): Dictionary mapping image numbers to probabilities of the next images, from transition_matrices.py
            color_matrix (dict): Dictionary mapping colors to probabilities of the next colors, from transition_matrices.py
        '''
        self.image_matrix = image_matrix
        self.color_matrix = color_matrix
        self.image_map = map_images()
        self.images = list(image_matrix.keys())
        self.colors = list(color_matrix.keys())

    def get_next_image(self, current_image):
        '''Chooses the next image based on the transition matrix
        
        Args:
            current_image (str): The last chosen image (number, as a string)

        Returns:
            Both the path to the next image and its corresponding number (1-16)
        '''
        next_image = np.random.choice(
            self.images,
            p=[self.image_matrix[current_image][n] for n in self.images]
        )
        return self.image_map[next_image], next_image

    def get_next_color(self, current_color):
        '''Chooses the next color based on the transition matrix
        
        Args:
            current_color (str): The last chosen color.

        Returns:
            The next color to be used (str)
        '''
        next_color = np.random.choice(
            self.colors,
            p=[self.color_matrix[current_color][c] for c in self.colors]
        )
        return next_color

    def get_next_pair(self, current_image, current_color):
        '''Return (image_path, color) as a coupled choice
        
        Args:
            current_image (str): The last chosen image number,as a string
            current_color (Str): The last chosen color

        Returns:
            (image_path, next_color) tuple, as well as next_image number, and next_color (to access easier)
        '''
        image_path, next_image = self.get_next_image(current_image)
        next_color = self.get_next_color(current_color)
        return (image_path, next_color), next_image, next_color