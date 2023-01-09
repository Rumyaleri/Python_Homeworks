# Задача 2.
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input('Ведите целое число: '))
factors = []
div = 2
while div <= num:
    if (num % div) == 0:
        factors.append(div)
        num = num // div
    else:
        div += 1
print(factors)

