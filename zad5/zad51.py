import random
Spisok = []
i = 0
j = 0
a = int(input("Угадайте одно из случайных чисел от 1 до 10: "))
for i in range(5):
    Spisok.append(random.randint(1, 10))
    i += 1
for i in range(5):
    if a == Spisok[i]:
        j += 1
    i += 1
if j > 0:
    print(Spisok,"\n", a,"\n", "Поздравляю, вы угадали число!")
else:
    print(Spisok,"\n", a,"\n", "Нет такого числа!")