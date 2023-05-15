mes=int(input())
if mes % 2 == 0 and mes > 0 and mes < 55:
    if mes < 37:
        print("Место верхнее, купе")
    else:
        print("Место верхнее, боковое")
elif mes % 2 != 0 and mes > 0 and mes < 55:
    if mes < 37:
        print("Место нижнее, купе")
    else:
        print("Место нижнее, боковое")
if mes <= 0 or mes >= 55:
    print("Неправильно введено место")