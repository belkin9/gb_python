"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(x, y):
    try:
        if (y < 0) & (x > 0):
            degree = 1
            for i in range(y, 0):
                degree = degree * x
            degree = 1 / degree
            return f"Для значений X = {x}, Y = {y} рузультат: {degree}"
        else:
            return "X должен быть положительным, Y должнен быть отрицательным"
    except TypeError:
        return "Пожалуйста, вводите только числа"

print(my_func(10, -4))
