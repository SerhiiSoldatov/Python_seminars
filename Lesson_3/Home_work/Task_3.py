# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

def func(n):
    line = ' '
    while n > 0:
        line = str(int(n%2))+line
        n //= 2
    return line
n = int(input('Введите число: '))
print(f'{n} -> {func(n)}')