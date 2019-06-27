# Тесты выполнены на 64-разрядной Win 10 версии 1803
# Python 3.7.2 [MSC v.1916 64 bit (AMD64)] on win32


import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, 'keys'):

            for j in var:
                print(f'\nПодпеременная: \'{j}\' весит {sys.getsizeof(j)}')

                if hasattr(var[j], '__iter__'):

                    if hasattr(var[j], 'keys'):
                        spam += memory_count([var[j]]) + sys.getsizeof(j)

                    else:
                        spam += memory_count(var[j]) + sys.getsizeof(j) + sys.getsizeof(var[j])

                else:
                    print(f'Вес его значения {var[j]}: {sys.getsizeof(var[j])}')
                    spam += sys.getsizeof(var[j]) + sys.getsizeof(j)

        else:

            if hasattr(var, '__iter__') and not isinstance(var, str):

                for j in var:
                    print(f'\nПодпеременная: {j} весит {sys.getsizeof(j)}')

                    if hasattr(j, '__iter__'):
                        spam += memory_count(j) + sys.getsizeof(j)

                    else:
                        spam += sys.getsizeof(j)

        memory += spam

    return memory


# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

# a = int(input('Введите целое трехзначное число:'))
#
# hundred = a // 100
# dozen = (a // 10) % 10
# unit = a % 10
#
# summa = hundred + dozen + unit
# mult = hundred * dozen * unit
#
# print(f'Сумма цифр в числе: {summa}')
# print(f'Произведение цифр в числе: {mult}')

# Затраты памяти программы:  168
# Переменные:  [234, 3, 2, 24, 9, 4]


# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# summa = (a // 100) + ((a // 10) % 10) + (a % 10)
# mult = (a // 100) * ((a // 10) % 10) * (a % 10)
#
# print(f'Сумма цифр в числе: {summa}')
# print(f'Произведение цифр в числе: {mult}')

# Затраты памяти программы:  84
# Переменные:  [234, 24, 9]


# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
# print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')

# Затраты памяти программы:  28
# Переменные:  [234]

# ВЫВОД: Использование дополнительных переменных занимает в памяти больше места, но их наличие порой облегчает
# читабельность кода. Сччитаю, что хорошим компромиссом этих критериев будет вариант 2.



# *******************Для проверки написанной функции на других типах переменных**************************
#  Определить, какое число в массиве встречается чаще всего.

# import random
#
#
# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 5
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print('Массив:', array, sep='\n')
#
# numbers = dict()
#
# for item in array:
#
#     if item not in numbers:
#         numbers[item] = 1
#
#     else:
#         numbers[item] += 1
#
# print(f'Повторения чисел в массиве:\n{numbers}')
#
# max_count = 0
# num_max_count = []
#
# for num in numbers:
#
#     if numbers[num] > max_count:
#         max_count = numbers[num]
#         num_max_count = [num]
#
#     elif numbers[num] == max_count:
#         num_max_count.append(num)
#
# print('\nЧаще всего встречается:', end=' ')
# print(*num_max_count)
# print(f'Количество повторений: {max_count}')


# Массив:
# [0, 0, 2, 5, 4, 2, 2, 0, 0, 3]
# Повторения чисел в массиве:
# {0: 4, 2: 3, 5: 1, 4: 1, 3: 1}
# # Чаще всего встречается: 0
# Количество повторений: 4
#
# Затраты памяти программы:  1232
# Переменные:  [5,              0,      10,    [0, 0, 2, 5, 4, 2, 2, 0, 0, 3],   3     ,     4,          3,     [0],        {0: 4, 2: 3, 5: 1, 4: 1, 3: 1}]
#             ['MAX_ITEM', 'MIN_ITEM',  'SIZE', 'array',                        'item', 'max_count', 'num', 'num_max_count', 'numbers']


# *******************Для проверки написанной функции на других типах переменных**************************
a = 1
b = [1, [2, 2], 3]
c = {'a': 1, 'ab': [2, 3], 'abc': {4: 5, '66': 7}}
d = 'abcd'

# Переменные:  [1, [1, [2, 2], 3], {'a': 1, 'ab': [2, 3], 'abc': {4: 5, '66': 7}}, 'abcd']
# Затраты памяти программы:  1293

# ***************************************************************************************************
print()
# собираем переменные для подсчета затрачиваемой памяти
_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))
