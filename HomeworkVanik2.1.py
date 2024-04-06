# Вывод ряда чисел Фибоначчи с помощью цикла while

fib1 = 1
fib2 = 1

n = int(input('Введите номер Фибоначи: '))

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)


# Вывод ряда чисел Фибоначчи с помощью цикла for

fib1 = fib2 = 1
n = int(input('Введите номер Фибоначи: '))

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
print(fib2)

# Рекурсивное вычисление n-го числа ряда Фибоначчи


def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n -1) + fib(n - 2)
n = int(input('Введите номер Фибаначи: '))
print(fib(n))