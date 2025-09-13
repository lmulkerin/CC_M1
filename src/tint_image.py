'''This is used to change the color palette of an image'''

from PIL import ImageOps

def tint_image(img, tint_color):
    gray = ImageOps.grayscale(img) # Convert to grayscale
    tinted = ImageOps.colorize(gray, black="black", white=tint_color)
    return tinted