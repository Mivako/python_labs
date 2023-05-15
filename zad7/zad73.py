from PIL import Image, ImageFilter
files = ["1.png", "2.png", "3.png", "4.png", "5.png"]
for file in files:
    with Image.open(file) as img:
        img = img.resize((img.width // 2, img.height // 2))
        img = img.convert("L")
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("zad73/" + str(file))