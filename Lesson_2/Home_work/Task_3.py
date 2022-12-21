# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.

num_list = []
sum = 0
n = int(input("Input your list's lengs: "))
for k in range(1, n+1):
    res = round((1 + 1/k) ** k, 3)
    num_list.append(res)
    sum = sum + res
print(num_list)
print(sum)
