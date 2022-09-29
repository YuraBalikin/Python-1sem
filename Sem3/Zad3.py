#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint
list = [randint(0, 100) for i in range(10)]
def mult_pairs (list):
    return [list[i] / 100 for i in range(len(list))]
print(mult_pairs (list))    
print(max(mult_pairs (list)))
print(min(mult_pairs (list)))    
print(max(mult_pairs (list))-min(mult_pairs (list)))   

