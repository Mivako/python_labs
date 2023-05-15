import random
Spisok = []
Spisok2 = []
i = 0
while i < 10:
    Spisok.append(random.randint(1, 30))
    i += 1
i = 0
j = 1
t = 0
while i < 10:
    while j < 10:
        if Spisok[i] == Spisok[j]:
            Spisok2.append(Spisok[i])
            t += 1
        j += 1
    j = i+2
    i += 1
if t > 0:
    print (Spisok, "\n", Spisok2)
else:
    print(Spisok, "\n", "Повторяющихся чисел нет")
