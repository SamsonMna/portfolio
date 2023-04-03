# Let's modify photos using Pillow module

from PIL import Image, ImageEnhance, ImageOps
# Compressing
im = Image.open('path to your image.jpg')
im.save('image.jpg', optimize=True, quality=90)

# Set Brightness
im = image.open('path tyo your image.jpg')
im = ImageEnhance.Bightness(im)
im = im.enhance(1.8)


# Croping
im = Image.open('path to image.jpg')
im = im.crop((0, 0, 0, 0)) # Give your crop parameters instead of the zeros

# Resizing
im = Image.open('path to image.jpg')
im = Image.resize((0, 0)) # Specify your resize parameters 

# Sharpening
im = Image.open('path to image.jpg')
IM = im.filter(ImageFilter.SHARPEN)

# Set contrast
im = Image.open('path to image.jpg')
im = ImageEnhance.Contrast(im)
im = im.enhance(0.0) # change the enhancement level to your liking

# Filters
im = Image.open('path to image.jpg')
im = ImageOps.grayscale(im)
im = ImageOps.invert(im)
im = ImageOps.posterize(im, 0) # change the zero to the level of posterity you wanna achieve.

# Save the image
im.save('path to file location')




