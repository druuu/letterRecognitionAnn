from PIL import Image, ImageDraw

size = 20, 20

im = Image.open("my_drawing.jpg")
im.thumbnail(size, Image.ANTIALIAS)
im.save("img", "JPEG")
            
