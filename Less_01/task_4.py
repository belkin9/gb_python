"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

number = int(input("Введите целое положительное число: "))
mx = 0
while number > 0:
    tmp = number % 10
    if tmp >= mx:
        mx = tmp
    number //= 10
print(f"Самая большая цифра в чилсе: {mx}")
