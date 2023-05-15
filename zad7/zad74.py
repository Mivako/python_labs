from PIL import Image, ImageFilter

with Image.open("logo.png") as logo:
    logo = logo.convert("L")
    threshold = 100
    logo = logo.point(lambda x: 255 if x < threshold else 0)
    logo = logo.resize((logo.width // 4, logo.height // 4))
    logo = logo.filter(ImageFilter.CONTOUR)
    logo = logo.point(lambda x: 0 if x == 255  else 255)
    logo = logo.crop((5, 5, 220, 220))

with Image.open("oh.png") as img:
    img.paste(logo, (120, 150), logo)
    img.show()