import os
from PIL import Image
import matplotlib.pyplot as plt

from pick_image_and_color import ImageAndColorChooser, map_images
from transition_matrices import IMAGE_MATRIX, COLOR_MATRIX
from background_remove import remove_background
from tint_image import tint_image

def generate_grid(rows, cols, start_image="1", start_color="cyan"):
    '''
    Generate a grid of tinted, background-removed images using Markov transitions
    
    Args:
        rows (int): number of rows in the grid
        cols (int): number of columns in the grid
        start_image (str): starting image number
        start_color (str): starting color

    Returns:
        One photo, composed of a grid of other modified photos.
    '''
    chooser = ImageAndColorChooser(IMAGE_MATRIX, COLOR_MATRIX)
    current_image, current_color = start_image, start_color
    processed_images = []

    for _ in range(rows * cols):
        (img_path, color), current_image, current_color = chooser.get_next_pair(current_image, current_color)
        img_no_bg = remove_background(img_path)
        img_tinted = tint_image(img_no_bg, color).convert('RGBA')
        processed_images.append(img_tinted)

    img_width, img_height = processed_images[0].size
    grid = Image.new("RGBA", (cols * img_width, rows * img_height))

    for idx, img in enumerate(processed_images):
        row, col = divmod(idx, cols) # quotient and remainder gives row, col to map into 2D grid
        grid.paste(img, (col * img_width, row * img_height), img)  # essentially overlay each image onto blank canvas (grid)

    return grid

if __name__ == "__main__":
    final_grid = generate_grid(3, 7, start_image="1", start_color="cyan")
    plt.imshow(final_grid)
    plt.axis("off")
    plt.show()