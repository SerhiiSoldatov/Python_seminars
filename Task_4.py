# Напишите программу которая на вход принимает дробь
# и показывает первую цифру дробной части числа

number = float(input())
new_num = int(number * 10 % 10)
print(new_num)