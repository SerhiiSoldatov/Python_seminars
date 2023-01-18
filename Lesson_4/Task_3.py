# На вход программе даётся число n.
# Программа печатает численный треугольник.
# Используеи вложенные циклы.

num = int(input())
for i in range(1, num + 1):
    for k in range(i):
        print(i, end = "")
    print()