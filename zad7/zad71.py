from PIL import Image
with Image.open("oh.png") as img:
    print(img.size, img.format, img.mode)
    img.show()