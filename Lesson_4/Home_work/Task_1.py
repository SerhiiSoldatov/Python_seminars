# 1. Вычислить число c заданной точностью d

import decimal
num1 = decimal.Decimal(input("Enter a real number: "))

print(num1)

a = int(input("Specify the required number of decimal places, like '3': "))
num2 = round(num1, a)
print(num2)

