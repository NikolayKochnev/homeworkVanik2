# Реализовать свой метод max
# Передаем в функцию список из чисел и он находит самое большое число и возвращает его

def large(n):
    max_ = n[0]
    for i in n:
        if i > max_:
            max_ = i
    return max_

list1 = [1, 2, 3, 4, 5, 6]
result = large(list1)
print(result)