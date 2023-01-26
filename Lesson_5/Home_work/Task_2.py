# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path

def rle_encode(text="file_1.txt", code="file_2.txt"):
    if path.exists(text):
        with open(text) as file_1, \
                open(code, "a") as file_2:
            for i in file_1:
                file_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))

def rle_decode(name):
    if path.exists(name):
        with open(name) as file:
            a = ""
            for b in file:
                num = []
                for i in b.strip():
                    if i.isdigit():
                        a += i
                    else:
                        num.append([int(a), i])
                        a = ""
                print("".join(starmap(lambda x, y: x * y, num)))


rle_encode(input("Text file: "), input("Record file: "))
print("----------------------------")
rle_decode(input("Decode file: "))


