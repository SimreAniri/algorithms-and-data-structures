# Определить, какое число в массиве встречается чаще всего.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив:', array, sep='\n')

numbers = dict()

for item in array:

    if item not in numbers:
        numbers[item] = 1

    else:
        numbers[item] += 1

print(f'Повторения чисел в массиве:\n{numbers}')

max_count = 0
num_max_count = []

for num in numbers:

    if numbers[num] > max_count:
        max_count = numbers[num]
        num_max_count = [num]

    elif numbers[num] == max_count:
        num_max_count.append(num)

print('\nЧаще всего встречается:', end=' ')
print(*num_max_count)
print(f'Количество повторений: {max_count}')
