#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

a = [int(i) for i in input().split()]
new_list = []
for i in a:
   if a.count(i) == 1:
    #    print(i)
    new_list.append(i)
print(new_list)