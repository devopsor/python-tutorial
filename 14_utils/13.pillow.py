#pip install pillow

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# random letters:
def rndChar():
    return chr(random.randint(65, 90))

# random color1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# random color2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# Create a Font object:
font = ImageFont.truetype('italic.otf', 36)
# Create a Draw object:
draw = ImageDraw.Draw(image)
# fill each pixel:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#output text:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# Vague:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')