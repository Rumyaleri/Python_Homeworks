# Задача 5.
# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1)

num = abs(int(input()))
# if num in [1, 2]:
#     print(1)
    
fib1 = fib2 = 1
list1 = [fib1, fib2]
for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    list1.append(fib2)

fib1 = fib2 = 1
for i in range(-num, 1):
     fib1, fib2 = fib2, fib1 - fib2
     list1.insert(0, fib2)
print(list1)
