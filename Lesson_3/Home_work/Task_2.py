# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def num_list(count: int):
    if count < 0:
        print("You can't use negative number!")
        return []

    num_list_2 = sample(range(1, count * 2), count)
    return num_list_2

def func(num_prod):
    sp_rezult = []
    for i in range(0,round((len(num_prod)+1)/2)):
        sp_rezult.append(num_prod[i]*num_prod[-i-1])
    return sp_rezult

num_list_2 = num_list(int(input("input length = ")))
print(num_list_2)
print(func(num_list_2))
