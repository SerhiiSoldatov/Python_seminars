# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.

def new_list(num):
    return [num for num in range(20, num + 1) if num % 20 == 0 or num % 21 == 0]


print(new_list(int(input("Введите верхнюю границу списка: "))))