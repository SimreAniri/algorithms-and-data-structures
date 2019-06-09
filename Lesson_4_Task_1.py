# Выбрана задача 1 из 3 урока

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import cProfile


MIN_DIV = 2
MAX_DIV = 9


def div_count(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = max_number // div

    return div_dict

# py -m timeit -n 100 -s "import Lesson_4_Task_1" "Lesson_4_Task_1.div_count(99)"
# "Lesson_4_Task_1.div_count(99)"
# 100 loops, best of 5: 795 nsec per loop
# "Lesson_4_Task_1.div_count(999)"
# 100 loops, best of 5: 809 nsec per loop
# "Lesson_4_Task_1.div_count(9999)"
# 100 loops, best of 5: 853 nsec per loop
# "Lesson_4_Task_1.div_count(99999)"
# 100 loops, best of 5: 858 nsec per loop
# Алгоритм работает приблизительно за O(1). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивалось незначительно. При увеличении количества входных элементов в 1000 раз время
#  увеличилось всего на 7,5%

# cProfile.run('div_count(9999)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:13(div_count)  99
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:13(div_count) 999
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:13(div_count)  9999
# Алгоритм работает быстро, в оптимизации не нуждается.


def div_count_dict(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = 0

        for num in range(2, max_number + 1):

            if num % div == 0:
                div_dict[div] += 1

    return div_dict

# py -m timeit -n 100 -s "import Lesson_4_Task_1" "Lesson_4_Task_1.div_count_dict(99)"
# "Lesson_4_Task_1.div_count_dict(99)"
# 100 loops, best of 5: 37 usec per loop
# "Lesson_4_Task_1.div_count_dict(999)"
# 100 loops, best of 5: 400 usec per loop
# "Lesson_4_Task_1.div_count_dict(9999)"
# 100 loops, best of 5: 4.22 msec per loop
# "Lesson_4_Task_1.div_count_dict(99999)"
# 100 loops, best of 5: 43.3 msec per loop
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count()

# cProfile.run('div_count_dict(99999)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:42(div_count_dict)   99
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:42(div_count_dict) 999
# 1    0.004    0.004    0.004    0.004 Lesson_4_Task_1.py:42(div_count_dict) 9999
# 1    0.046    0.046    0.046    0.046 Lesson_4_Task_1.py:42(div_count_dict) 99999
# Рекурсий в алгоритме нет, время выполнения нарастает линейно.


def div_count_xxxx(max_number):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, max_number + 1):

        if num % 2 == 0:
            div_dict[2] += 1

        if num % 3 == 0:
            div_dict[3] += 1

        if num % 4 == 0:
            div_dict[4] += 1

        if num % 5 == 0:
            div_dict[5] += 1

        if num % 6 == 0:
            div_dict[6] += 1

        if num % 7 == 0:
            div_dict[7] += 1

        if num % 8 == 0:
            div_dict[8] += 1

        if num % 9 == 0:
            div_dict[9] += 1

    return div_dict

# py -m timeit -n 100 -s "import Lesson_4_Task_1" "Lesson_4_Task_1.div_count_xxxx(99)"
# "Lesson_4_Task_1.div_count_xxxx(99)"
# 100 loops, best of 5: 31.8 usec per loop
# "Lesson_4_Task_1.div_count_xxxx(999)"
# 100 loops, best of 5: 331 usec per loop
# "Lesson_4_Task_1.div_count_xxxx(9999)"
# 100 loops, best of 5: 3.4 msec per loop
# "Lesson_4_Task_1.div_count_xxxx(99999)"
# 100 loops, best of 5: 35.1 msec per loop
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count(),
# при этом этот алгоритм чуть быстрее, чем div_count_dict()

# cProfile.run('div_count_xxxx(99999)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:75(div_count_xxxx)   99
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:75(div_count_xxxx) 999
# 1    0.004    0.004    0.004    0.004 Lesson_4_Task_1.py:75(div_count_xxxx) 9999
# 1    0.037    0.037    0.037    0.037 Lesson_4_Task_1.py:75(div_count_xxxx) 99999
# Рекурсий в алгоритме нет, время выполнения нарастает линейно.



# MAX_NUMBER = 99
#
# print(div_count(MAX_NUMBER))
# print(div_count_dict(MAX_NUMBER))
# print(div_count_xxxx(MAX_NUMBER))
