Korteg = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
Spisok1 = []
Spisok2 = []
a = int(input("Сколько вы хотите выходных? "))
for i in range(a):
    Spisok1.append(Korteg[7-a+i])
for i in range((7-a)):
    Spisok2.append(Korteg[i])
print("Ваши выходные дни: ", Spisok1)
print("Ваши рабочие дни: ", Spisok2)