# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

from random import randint

def my_list (size, m, n):
    return [randint(m, n) for i in range (size)]
size  =  10
m = 1
n = 10
list = my_list (size, m, n)
print (list)
#list = [1, 2, 3, 5, 1, 5, 3, 10]
# так
result_list = []
for i  in list:
    if list.count(i) == 1:
        result_list.append(i)
print(result_list)
# или так 
print([i for i in list if list.count(i) == 1])



