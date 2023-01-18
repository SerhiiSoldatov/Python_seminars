# Задайте список, состоящий из произвольных чисел, кол-во задаёт пользователь.
# Напишите программу, определяющую, присутствует ли в заданном списке число, полученое от пользователя.

from random import sample

def num_find(len_list, num):
    new_list = sample(range(1, len_list * 2), k = len_list)
    print(new_list)
    if num in new_list:
        return 'Yes'
    return 'No'

print(num_find(int(input("input list's lengs: ")), int(input("input number: "))))

