i = 0
print("Для завершения программы введите слово 'стоп'")
while(1>0):
    word = input()
    if word == "стоп":
        break
    else:
        for a in word:
            if a == "ф" or a == "Ф":
                i += 1
        if i>0:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
    i = 0