# Задача 1. Напишите программу, которая 
#     - принимает на вход цифру, обозначающую день недели, и 
#     - проверяет, является ли этот день выходным.
#     Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

x= int(input('Введите номер дня недели: '))
if x > 5 and x < 8:
    print('Yes')
elif x >= 1 and x < 6:
    print('No')
else:
    print('uncorrect number')