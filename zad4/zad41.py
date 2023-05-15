def tri(a):
    if a % 3 == 0:
        print("Введенное число кратно 3")
    else:
        print("Введенное число не кратно 3")

x = int(input("введите число: "))
tri(x)