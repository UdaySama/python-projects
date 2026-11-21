import barcode
from barcode.writer import ImageWriter
from PIL import Image

user_data = input("Enter the data: ")
code = barcode.get('code128', user_data, writer=ImageWriter())
fileName = code.save('sidbarcode')

img = Image.open(fileName)
img.show()

