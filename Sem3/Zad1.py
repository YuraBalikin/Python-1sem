#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


from random import randint
list = [randint(0, 10) for i in range(10)]
print(list)
#print(sum(list[1::2]))
def getSumOdds(list):
    result = 0
    for i in range(1,len(list),2):
        result += list[i]
    return result
print(getSumOdds(list))    