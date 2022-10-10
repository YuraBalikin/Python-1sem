# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
def sum_num(num: str) -> int:
    return sum(map(int, filter(lambda i: i.isdigit(), str(num))))
print(sum_num(-6782))
print(sum_num(0.56))


#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

def fact(n: int) -> list:
    lst =[i for i in range(1, n+1)]
    fact = list(map(lambda x: math.factorial(x), lst))
    return fact
   
print(fact(4))

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

input = [1.1, 1.2, 3.1, 5, 10.01]
print(max(map(fract:= lambda x: float(fr:=str(x).split('.')[1])/10**(len(fr)), input)) - min(map(fract, input)))







    