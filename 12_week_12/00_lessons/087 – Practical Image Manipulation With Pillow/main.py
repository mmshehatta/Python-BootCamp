from PIL import Image
from urllib.request import urlopen
# Open The Image
url = "https://python-pillow.org/images/pillow-logo.png"
# myImage = Image.open("week_12/00_lessons/087 – Practical Image Manipulation With Pillow/image.jpeg")
myImage = Image.open(urlopen(url))
# Show The Image
myImage.show()
# My Cropped Image
myBox = (10, 10, 50, 50)
myNewImage = myImage.crop(myBox)
# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()
