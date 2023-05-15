import random
t = 0
f = 0
while(1>0):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a,"+",b, "= ", end = "")
    otvet = int(input())
    if otvet == a+b:
        print("Правильно!")
        t += 1
    else:
        print("Ответ неверный")
        f += 1
    if f == 3:
        break
print("Игра окончена. Правильных ответов: ", t)