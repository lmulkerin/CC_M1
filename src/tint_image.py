'''This is used to change the color palette of an image'''

from PIL import ImageOps

def tint_image(img, tint_color):
    '''Change the entire color palette of an image.
    
    Args:
        tint_color (str): Desired color for tint (cyan, magenta, lime, dodgerblue,orchid, yellow, or darkorange)

    Returns:
        A tinted image object
    '''
    gray = ImageOps.grayscale(img) # Convert to grayscale
    tinted = ImageOps.colorize(gray, black="black", white=tint_color)
    return tinted