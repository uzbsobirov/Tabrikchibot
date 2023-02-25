from PIL import Image, ImageDraw, ImageFont

# img = Image.open("media/1-type.jpg")
# draw = ImageDraw.Draw(img)
# text = "Hello, World!"
# font = ImageFont.truetype("media/PleasantlyPlump-pRv1.ttf", 48)
# text_size = draw.textbbox((100, 100), text, font=font)
#
# x = 400
# y = 330
#
# draw.text((x, y), text, font=font, fill='black')
#
# img.save("media/results.jpg")
# img.show()

temp_image = Image.new(mode='RGB', size=(400, 200), color=(255, 255, 255))
font = ImageFont.truetype('arial.ttf', size=30)
draw = ImageDraw.Draw(temp_image)
text = 'Rotated Text'
draw.text((100, 75), text, font=font, fill=(0, 0, 0))
rotated_text = temp_image.rotate(30, expand=True)
image = Image.new(mode='RGBA', size=rotated_text.size, color=(0, 0, 0, 0))
image.paste(rotated_text, (0, 0), rotated_text)
image.show()

