# Задача 18.
# Реализуйте алгоритм перемешивания списка.

import random
list_1 = [random.randint(-15,15) for i in range(10)]
print ('Исходный список: ' + str(list_1))
random.shuffle(list_1)
print ('Перетасованный список: ' +  str(list_1))