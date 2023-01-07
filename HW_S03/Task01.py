# Задача 1.
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


 
 # ищем элементы, стоящие на нечетных позициях - т.е. первый, третий, пятый и т.д. 

import random
list = [random.randint(0,10) for i in range(10)]
print (list)
sum = 0
for i in range(len(list)):
    if i % 2 == 0:
        sum = sum + list[i]
print(sum)    


  # ищем элементы с нечетными индексами.

import random
list = [random.randint(0,10) for i in range(10)]
print (list)
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print(sum)  