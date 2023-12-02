"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def get_max1(*args):
    print(sum(sorted(list(args), reverse = True)[:1]))

def get_max2(*args):
    lst = list(args)
    i = 0
    j = 0
    while i != 2:
        max_value = max(lst)
        j += max_value
        lst.remove(max_value)
        i += 1
    print(j)

get_max1(100, 1, 200)
get_max2(700, 6, 99)
