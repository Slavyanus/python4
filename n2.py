# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))
while n > 1:
    i = 2
    f = 0
    while 1:
        if n%i == 0:
            n = n // i
            print(i, end=' ')
            f = 1
            break
        else:
            i += 1
    if f == 1:
        continue
print()