# Задача .
# Напишите программу, которая 
# - принимает на вход число N и 
# - выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите целое число: '))
def factorialRow(n):
    f = 1
    list = []
    for i in range(1, n+1):
       f *= i
       list.append(f)
    return list
print(factorialRow(n))
