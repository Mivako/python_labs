Line = ""
while(1>0):
    word = input()
    if word != "stop":
        Line += word + " "
    else:
        break
print(Line)