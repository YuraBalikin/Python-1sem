num = int(input('Введите число n: '))
def DecimalToBinary(num):
    strs = ""
    while num:
        if (num & 1):
            strs += "1"
        else:
            strs += "0"
        num >>= 1
    return strs
def reverse(strs):
    print(strs[::-1])
 

print('Для вашего числа это: ', end=" ")
reverse(DecimalToBinary(num))