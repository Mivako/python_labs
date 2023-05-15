one = {'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}
two = {'д', 'к', 'л', 'м', 'п', 'у'}
three = {'б', 'г', 'ё', 'ь', 'я'}
four = {'й', 'ы'}
five = {'ж', 'з', 'х', 'ц', 'ч'}
eight = {'ш', 'э', 'ю'}
ten = {'ф', 'щ', 'ъ'}

s = 0
word = input("Введите слово: ")
for i in word:
    if i in one:
        s += 1
    elif i in two:
        s += 2
    elif i in three:
        s += 3
    elif i in four:
        s += 4
    elif i in five:
        s += 5
    elif i in eight:
        s += 8
    elif i in ten:
        s += 10
print("Стоимость слова: ", s)