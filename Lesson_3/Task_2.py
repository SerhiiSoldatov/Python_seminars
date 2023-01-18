# Задайте список, состоящий из произвольных слов, кол-во задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке, либо сообщит, что её нет.

from random import sample

def list_1 (words_count, word = "abc"):
    my_list = []
    for i in range (words_count):
        temp_word = sample (word, k = 3)
        my_list.append("".join(temp_word))
    return my_list

def find_index (word, list_2):
    if word in list_2 and list_2.count(word) > 1:
        first_index = list_2.index(word)
        print (list_2.index(word, first_index + 1))
    else:
        print(-1)

first_def_list = list_1(int(input("input words_count: ")))

print (first_def_list)

find_index (input("print word, what you tri finding: "), first_def_list)