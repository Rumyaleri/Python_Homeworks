# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input())
temp = 0
count = 1
while num > 0:
    temp = temp + num % 2 * count
    num = num // 2
    count = count * 10
print(temp)
