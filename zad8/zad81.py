from PIL import Image

with Image.open("otkrytka.jpeg") as img:
    img = img.resize((img.width // 2, img.height // 2))
    img = img.crop((0,0,800,350))
    img.show()
    img.save("new_otkrytka.jpeg")

