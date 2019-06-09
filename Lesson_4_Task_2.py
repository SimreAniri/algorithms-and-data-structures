# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# Тестовая функция проверяет до 1229-го простого числа.

import cProfile

# def test(num, n=10000):
#     sieve = [i for i in range(n)]
#     sieve[1] = 0
#
#     for i in range(2, n):
#         if sieve[i] != 0:
#             j = i + i
#             while j < n:
#                 sieve[j] = 0
#                 j += i
#
#     res = [i for i in sieve if i != 0]
#     print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')
#
#     assert num < len(res)
#     return res[num - 1]


def eratosthenes_sieve(n):
    count = 0
    start = 0
    end = 3 * n

    sieve = [i for i in range(start, end)]
    sieve[1] = 0

    prime = []

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += i

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 1 * n
        sieve = [i for i in range(start, end)]

        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0

# py -m timeit -n 100 -s "import Lesson_4_Task_2" "Lesson_4_Task_2.eratosthenes_sieve(10)"
# "Lesson_4_Task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 5.49 usec per loop
# "Lesson_4_Task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 1.51 msec per loop
# "Lesson_4_Task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 215 msec per loop
# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения более, чем в 100 раз

# cProfile.run('eratosthenes_sieve(10)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:30(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:35(<listcomp>)
# cProfile.run('eratosthenes_sieve(100)')
# 1    0.002    0.002    0.002    0.002 Lesson_4_Task_2.py:30(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:35(<listcomp>)
# 3    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:56(<listcomp>)
# 3    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:59(<listcomp>)
# cProfile.run('eratosthenes_sieve(1000)')
# 1    0.203    0.203    0.203    0.203 Lesson_4_Task_2.py:30(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:35(<listcomp>)
# 5    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:56(<listcomp>)
# 5    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:59(<listcomp>)
# Время выполнения нарастает. Рекурсий нет.


# n = 1000
# if eratosthenes_sieve(n) == test(n):
#     print(f'{n}-ое простое число {eratosthenes_sieve(n)}')
#     print('OK')
