# Задача 16
# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06


def sequence(n):
    list = []
    for i in range (1, n+1):
        list.append(round((1+1/i)**i, 2))
    return list

def sum(list):
    sum=0
    for i in range (len(list)):
        sum=sum + list[i]
    return sum

n = int(input('Введите число N: '))

list = sequence(n)
print(list)
result = sum(list)
print(result)

