#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
import math
list = [randint(0, 10) for i in range(5)]
print(list)
def mult_pairs (list):
    return [list[i] * list[-i - 1] for i in range(math.ceil(len(list)/2))]
print(mult_pairs (list))    