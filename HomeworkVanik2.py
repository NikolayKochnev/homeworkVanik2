# Вычисление факториала циклом while
number = int(input('Введите число: '))
factorial = 1

while number > 1:
    factorial = factorial * number
    number = number - 1

print(factorial)


# Цикл for
number = int(input('Введите число: '))
factorial = number

for i in range(1, number):
    factorial = factorial * i

print(factorial)


# Вычисление факториала Рекурсией

def factorial(number):
    if number == 1 or number == 0:
        return number
    else:
        return number * factorial(number - 1)

print(factorial(int(input('Введите число: '))))



