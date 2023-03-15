# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
import os
def clear(): return os.system('cls')
clear()

size_list = int(input("Введите колличество элементов массива - "))
some_list = [randint(-10, 10) for i in range(size_list)]
low_number = int(input("Введите нижнюю границу - "))
high_number = int(input("Введите верхнюю границу - "))
print(some_list)
for i in range(len(some_list)):
    if low_number <= some_list[i] <= high_number:
        print(i,end=' ')