import random
MV4 = ["Николаева", "Соколова", "Веселова", "Дзбоева", "Родионова", "Крупницкий", "Мигунов", "Калашникова", "Денисова", "Коллар"]
MV5 = ["Тоноян", "Иванов", "Юрина", "Грищенко", "Королева", "Войченко", "Михайлова", "Бекренёва", "Григорьева", "Шелькова"]
Komanda = (MV4[random.randint(0, 1)], MV4[random.randint(2, 3)], MV4[random.randint(4, 5)], MV4[random.randint(6, 7)], MV4[random.randint(8, 9)], MV5[random.randint(0, 1)], MV5[random.randint(2, 3)], MV5[random.randint(4, 5)], MV5[random.randint(6, 7)], MV5[random.randint(8, 9)])
print(MV4)
print(MV5)
print(Komanda)
print(len(Komanda))
Komanda = tuple(sorted(Komanda))
print(Komanda)
b = Komanda.count("Иванов")
if b > 0:
    print("Ивановых в команде: ", b)
else:
    print("Ивановых нет в команде")