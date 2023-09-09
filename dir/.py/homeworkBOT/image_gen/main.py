from PIL import Image, ImageDraw, ImageFont
import os

cont = "Mathe: Buch S. 15 Nr. 3\nDeutsch: Buch S. 147 Nr. 16 a, b, c\nEnglisch: Buch S. 185 Nr. 9, 12\nGeschichte: Buch S. 88 Nr. 3 a, b, c; 4 b, c"

path = os.path.dirname(__file__) + '/'
img = Image.open("image.png")
draw = ImageDraw.Draw(img)
fnt = ImageFont.truetype("font.ttf", 23)
draw.text((115, 80), cont, font=fnt, fill=(255, 255, 255))
img.save("img/image_4.png")