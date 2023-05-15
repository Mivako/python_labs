def mas(s):
    l = len(s)
    i = 0
    j = 0
    while i < l:
        s_int = ''
        while i < l and '0' <= s[i] <= '9':
            s_int += s[i]
            i += 1
        i += 1
        if s_int != '':
            if j == 0:
                a = int(s_int)
                j += 1
            elif j == 1:
                b = int(s_int)
                j += 1
            elif j == 2:
                c =  int(s_int)
                j += 1
    if a * b == (c % 100):
        return True
    else:
        return False

mag = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if mas(mag) == True:
    print("Это магическая дата")
else:
    print("К сожалению, это не магическая дата")
