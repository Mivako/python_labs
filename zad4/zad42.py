def sto(a):
    try:
        b = float(a)
        if b > 0 or b < 0 :
            return 100 / b
        else:
            return "Введенное число невозможно в качестве делителя"
    except:
        return "Введенный текст не является числом"

x = input()
print(sto(x))