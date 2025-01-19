# %%
from PIL import Image
import pytesseract


def read_image_from_file(image_path):
    return Image.open(image_path)


def read_text_from_image(image):
    return pytesseract.image_to_string(image)
