# Задача 3.
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import random
list = [random.randint(0,10) for i in range(15)]
list2 = []
for i in list:
    if list.count(i) == 1:
        list2.append(i)
print (list)
print(list2)