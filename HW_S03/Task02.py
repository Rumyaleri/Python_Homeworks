# Задача 2.
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
list = [random.randint(0,5) for i in range(10)]
list1 = []
for i in range(len(list)//2):
    list1.append(list[i]*list[-i - 1])
print (list)
print(list1)