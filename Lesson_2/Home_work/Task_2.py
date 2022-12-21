# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

num_list = []
mult = 1
num = int(input("Input your number: "))
for i in range(1, num):
    mult = mult * (i + 1)
    num_list.append(mult)
print(num_list)