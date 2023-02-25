from PIL import Image, ImageDraw, ImageFont

img = Image.open("media/1-type.jpg")
draw = ImageDraw.Draw(img)
text = "Hello, World!"
font = ImageFont.truetype("media/PleasantlyPlump-pRv1.ttf", 48)
text_size = draw.textbbox((100, 100), text, font=font)

x = 400
y = 330

draw.text((x, y), text, font=font, fill='black')

img.save("media/results.jpg")
img.show()
