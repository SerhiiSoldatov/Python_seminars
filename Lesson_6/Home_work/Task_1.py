# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample


def more_then(num):
    new_list = sample(range(num * 3), num)
    print(new_list)
    return [new_list[num] for num in range(1, len(new_list)) if new_list[num] > new_list[num - 1]]


print(more_then(int(input("Введите число: "))))