# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9

count = {i: 0 for i in range(MIN_DIV, MAX_DIV + 1)}

for div in range(MIN_DIV, MAX_DIV + 1):
    count[div] = MAX_NUMBER // div

print('Делитель    Чисел на него делится')
for div in count:
    print(f'{div:>6}  {count[div]:>16}')
