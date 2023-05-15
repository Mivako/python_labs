from PIL import Image
d = {1: "821.jpg", 2: "822.jpg", 3: "823.jpg", 4: "824.jpg"}

print("1 - Новый год\n"
      "2 - 23 февраля\n"
      "3 - 8 марта\n"
      "4 - День рождения")
x = int(input("Для получения открытки введите число - номер прадника : "))

file = d[x]
with Image.open(file) as img:
    img.show()