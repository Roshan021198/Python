from PIL import Image, ImageFilter

# Creating a image filter
im1 = Image.open(r"putta.jpg")

# applying varius filter

im2 = im1.filter(ImageFilter.BLUR)
im3 = im1.filter(ImageFilter.CONTOUR)
im4 = im1.filter(ImageFilter.EMBOSS)
im5 = im1.filter(ImageFilter.EDGE_ENHANCE)

# showing Result
im2.show()
im3.show()
im4.show()
im5.show()