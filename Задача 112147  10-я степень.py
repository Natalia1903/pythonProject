# Напишите программу, которая возводит введенное число в степень 10.
#
# Входные данные
#
# Входная строка содержит единственное вещественное число в диапазоне от 0 до 8.
#
# Выходные данные
#
# Нужно вывести 10-ю степень полученного числа с тремя знаками в дробной части

#c
a = float(input())
t = a**10
print("%.3f" %t)

#format
a = float(input())
t = a**10
print("{:.3f}".format(t))

#f
a = float(input())
print(f"{a**10:.3f}")