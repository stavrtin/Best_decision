# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
# from random import randint

# def choise_params():
#     # def guest_number(max_number, count=3):
#     input_max_step = int(input(f'{"Введите число попыток "}'))
#     input_max_number = int(input(f'{"Введите макс число интервала "}'))
#     def guest_number():
#         count = input_max_step
#         max_number = input_max_number
#         guest = randint(0, max_number)
#         step = 0
#         while count > step:
#             res = int(input(f'{"Введите число "}'))
#             step += 1
#             if res == guest:
#                 return print(f'Вы угадали за {step} хода')
#             elif res > guest:
#                 print('Бери меньше')
#             elif res < guest:
#                 print('Бери больше')
#
#         return print(f'Вы не угадали за {step} хода')
#
#     return guest_number()
#
# -------------------------------------------------------------------------------------------------------
# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
#
# from typing import Callable
# from random import  randint
#
# def deco(func: Callable):
#     MIN_COUNT = 1
#     MAX_COUNT = 10
#     MAX_NUM = 100
#     MIN_NUM = 1
#     def wrapper(*args, ** kvarg):
#         count, number = args
#         if count > MAX_COUNT or count < MIN_COUNT:
#             count = randint(MIN_COUNT, MAX_COUNT)
#         if number > MAX_NUM or number < MIN_NUM:
#             number = randint(MIN_NUM, MAX_NUM)
#         return func(count, number)
#     return wrapper
#
#
# @deco
# def choise_params(count, guest):
#     def guest_number():
#         for i in range(1, count + 1):
#             res = int(input(f'{"Введите число "}'))
#             if res == guest:
#                 print(f'Вы угадали за {i} хода')
#                 break
#             elif res > guest:
#                 print(f'Бери меньше')
#             elif res < guest:
#                 print(f'Бери больше')
#
#         else: print(f'Вы не угадали за {count} попыток')
#
#     return guest_number
#
# choise_params(10,110)()

'''Задание №3
📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она 
возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции.'''
# import json
# from typing import Callable
#
# def deco(func: Callable):
#     data = {}
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         data.update({**kwargs})
#         with open(f'{func.__name__}.json', 'a') as f:
#             json.dump(data, f)
#
#
#     return wrapper
#
#
# @deco
# def multy(a: int, b: int, *args, **kwargs) -> int:
#     res_m = a * b
#     return res_m
#
#
# multy(2,3, c=2, d=4)


'''Задание №4
📌 Создайте декоратор с параметром. 
📌 Параметр - целое число, количество запусков декорируемой 
функции. '''
from typing import Callable

def count_par(param: int):
    def deco(func: Callable):
        res_list = []
        def wrapper(*args, **kwargs):

            for i in range(param):
                res_list.append(func(*args, **kwargs))

            return res_list
        return wrapper
    return deco

@count_par(5)
def fact(num: int) -> int:
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

print(fact(5))