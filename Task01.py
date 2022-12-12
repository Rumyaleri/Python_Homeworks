# # 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# #     *Примеры:*

# #     - 5, 25 -> да
# #     - 4, 16 -> да
# #     - 25, 5 -> да
# #     - 8,9 -> нет

# a = int(input('Введите а '))
# b = int(input('Введите b '))

# if (a == b**2 or b == a**2):
#     print('Да')
# else:
#     print('Нет')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# a = int(input('Введите а '))
# b = int(input('Введите b '))
# c = int(input('Введите c '))
# d = int(input('Введите d '))
# e = int(input('Введите e '))

# max = a
# if b > a:
#     max = b
# if c > b:
#     max = c
# if d > c:
#     max = d
# if e > d:
#     max = e
# print(f"{max}")


# a = int(input())
# maxx = a
# for i in range(4):
#     a = int(input())
#     if a>maxx:
#         maxx = a
# print(maxx)

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# def prompt(msg):
#     print(msg)
#     num = int(input())
#     return num

# def list_num(num):
#     list = []
#     for i in range(-num, num+1):
#         list.append(i)
#     return list

# n = prompt("Enter n")
# list_n = list_num(num = n)
# print(f"{list_n} ")


# 2. Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.
#     *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# def prompt(msg):
#     print(msg)
#     num = float(input())
#     return num

# def first_num(numb):
#     first_num = int((num * 10)) % 10
#     return first_num

# num = prompt("Enter a number")
# first_numb = first_num(numb = num)
# print(f" first number = {first_numb}")


# a=float(input('Введите число: '))
# b = int((a*10)%10)
# print(b)

#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# n = float(input())
# print(int(n*10%10))
n = input()
a=n.split(".")
print(a[1][0])


# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = int(input('Введите число: '))
if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and (a % 30 != 0):
    print('yes')
else:
    print('no')

# #3. Напишите программу, которая принимает на вход число и проверяет,
# # кратно ли оно 5 и 10 или 15, но не 30.

# def prompt(msg):
#     print(msg)
#     num = int(input())
#     return num

# def check_div(number):
#     if (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0 and number % 30 != 0):
#         return True
#     else:
#         return False

# number  = prompt("Enter a number ")
# if check_div(number) == True:
#     print("Everything is all righ ")
# else:
#     print("No")
