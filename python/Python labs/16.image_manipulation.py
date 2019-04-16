# 16.image_manipulation.py
from PIL import Image
img = Image.open('leanna.png')
width, heigth = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        pixels[i,j] = (r, g, b)
img.show
