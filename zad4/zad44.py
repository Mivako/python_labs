def bil(s):
    l = len(s)
    i = 0
    ch1 = 0
    ch2 = 0
    while i < (l / 2):
        a = int(s[i])
        ch1 += a
        i += 1
    while i < l:
        a = int(s[i])
        ch2 += a
        i += 1
    if ch1 == ch2:
        return print("Ого, это счастливый билет!")
    else:
        return print("Обычный билет, ничего удивительного")

bilet = input("Введите номер билета: ")
bil(bilet)