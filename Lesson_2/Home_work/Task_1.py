# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

num = input("num = ")
sum = 0

num_len = len(num) - 2
num = float(num)
num = num * (10 ** num_len)
# print(num)
while num:
    sum = sum + int(num % 10)
    num = num / 10
print(sum)
