import os
import numpy as np

'''This chooses an image and a color based on transition matrices, then returns them as a tuple'''

# This was needed to access images properly:
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from src/
IMAGE_DIR = os.path.join(BASE_DIR, "images")


def map_images():
    image_map = {}
    for file in os.listdir(IMAGE_DIR):
        name, ext = os.path.splitext(file)
        if name.isdigit():
            image_map[name] = os.path.join(IMAGE_DIR, file)
    return image_map


class ImageAndColorChooser:
    def __init__(self, image_matrix, color_matrix, image_map):
        self.image_matrix = image_matrix
        self.color_matrix = color_matrix
        self.image_map = image_map
        self.images = list(image_matrix.keys())
        self.colors = list(color_matrix.keys())

    def get_next_image(self, current_image):
        """Return the next image path based on transition matrix"""
        next_image = np.random.choice(
            self.images,
            p=[self.image_matrix[current_image][n] for n in self.images]
        )
        return self.image_map[next_image], next_image

    def get_next_color(self, current_color):
        """Return the next color based on transition matrix."""
        next_color = np.random.choice(
            self.colors,
            p=[self.color_matrix[current_color][c] for c in self.colors]
        )
        return next_color

    def get_next_pair(self, current_image, current_color):
        """Return (image_path, color) as a coupled choice"""
        image_path, next_image = self.get_next_image(current_image)
        next_color = self.get_next_color(current_color)
        return (image_path, next_color), next_image, next_color
