# Задача 3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
list = [round(random.uniform(0, 10), 2) for i in range(10)]
list1 = []
for i in range(len(list)):
    list1.append(round(list[i], 2) - int(list[i]))
result = round(max(list1) - min(list1), 2)
print (list)
print(result)
