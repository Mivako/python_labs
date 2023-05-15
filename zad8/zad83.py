from PIL import Image, ImageDraw, ImageFont


name = input("Введите имя получателя: ")
file = "new_otkrytka.jpeg"
with Image.open(file) as img:
    img.load()
font = ImageFont.truetype("arial_bold.ttf", 40)
x = ImageDraw.Draw(img)
x.text(
    (img.width // 2 - 180, 280),
    name + ", поздравляю!",
    font=font,
    fill=('#FAACAC')
)
img.show()
img.save(name + "_otkrytka.png")