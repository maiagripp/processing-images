from PIL import Image
import os

filelist = [
    "images/girlface.bmp",
    "images/houses.bmp",
    "images/lena_color.bmp",
    "images/lena512.bmp",
    "images/Mercury.bmp",
    "images/pens.bmp",
]

img = Image.open("images/moon.jpg")
# Converting images to png
# for infile in filelist:
#     outfile = os.path.splitext(infile)[0] + ".png"
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print("Cant convert file"), infile

# Opening a image
# img = Image.open("images/profile.jpg")
# img.show()

# Converting image to grayscale
# new_img = Image.open("images/profile.jpg").convert("L")
# new_img.show()

# Resizing image
smaller_image = img.resize((150, 150))
# smaller_image.show()
# Crop images
box = (100, 100, 400, 400)
region = img.crop(box)
# region.show()

# Rotation image
rotated_img = img.rotate(90)
# rotated_img.show()
