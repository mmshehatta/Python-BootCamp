# >> 00 Lesson
# >> 08 Functions
# >> 087 - Practical Image Manipulation With Pillow.py
from icecream import ic

#############################################################
# >> 087 - Practical Image Manipulation With Pillow.py
#############################################################

from PIL import Image
import os
# OPen Image:
myImage = Image.open("/home/mahmoud/Pictures/Wallpapers/IMG_20210110_160041.jpg")
myImage.show()

myBox = (300,300,1000,1000)
newImg = myImage.crop(myBox)
newImg.show()

