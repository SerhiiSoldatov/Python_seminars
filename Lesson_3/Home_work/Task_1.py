# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def num_list(count: int):
    if count < 0:
        print("You can't use negative number!")
        return []

    num_list_2 = sample(range(1, count * 2), count)
    return num_list_2

def nums_sum(list_nums: list):
    sum = 0
    for i in range(0, len(list_nums), 2):
        sum = sum + list_nums[i]
    return sum


num_list_3 = num_list(int(input("input length = ")))
print(num_list_3)
print(nums_sum(num_list_3))