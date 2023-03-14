from PIL import Image
def add_img(img_path, width, height):
    """Read and return a resized logo"""
    img = Image.open(img_path)
    modified_img = img.resize((width, height))
    return modified_img