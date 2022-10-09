# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности

from random import randint as r
ulist = {}
fStr = ""
ListStr = "".join(list(map(str,[r(0,9) for i in range(20)])))
print (f"Задана последовательность цифр {ListStr}")
for c in ListStr:
        if ulist.get(c):
            ulist[c] = ulist.get(c) +1 
        else:
            ulist[c] = 1
for i in ulist.items():
    if i[1] == 1:
        fStr += str(i[0])

print (f"Уникальные цифры {fStr}") if fStr else print ("Уникальных позиции нет")