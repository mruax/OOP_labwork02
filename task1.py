def my_abs(num):
    if num < 0:
        num *= -1
    return num


def my_min(a, b):
    if a > b:
        return b
    return a


def my_max(a, b):
    if a > b:
        return a
    return b


a, b = int(input("Введите число a: ")), int(input("Введите число b: "))
print(f"Сумма чисел = {a + b}")
print(f"Разность чисел = {a - b}")
print(f"Произведение чисел = {a * b}")
print(f"Среднее арифметическое чисел = {(a + b) / 2}")
print(f"Разность макс. и мин. по модулю = {my_max(my_abs(a), my_abs(b)) - my_min(my_abs(a), my_abs(b))}")
