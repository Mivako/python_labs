god = int(input())
if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0):
    print("Год",god,"- високосный")
else:
    print("Этот год не високосный")