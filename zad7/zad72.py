from PIL import Image
with Image.open("oh.png") as img:
    lofi = img.resize((img.width // 3, img.height //3))
    lofi1 = lofi.transpose(Image.FLIP_TOP_BOTTOM)
    lofi2 = lofi.transpose(Image.FLIP_LEFT_RIGHT)
    lofi1.save("oh1.png")
    lofi2.save("oh2.png")