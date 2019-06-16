# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def sum_hex(x, y):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    while len(x) and len(y):
        res = hex_num[x.pop()] + hex_num[y.pop()] + transfer
        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    while len(x):
        res = hex_num[x.pop()] + transfer
        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    while len(y):
        res = hex_num[y.pop()] + transfer
        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return result


print('Для ввода шестнадцатиричных чисел используйте:')
print('0 1 2 3 4 5 6 7 8 9 A B C D E F\n')
a = deque(input('Введите 1-е шестнадцатиричное число: '))
b = deque(input('Введите 2-е шестнадцатиричное число: '))
# print(a, b)

print(*a, '+', *b, '=', end=' ')
print(*sum_hex(a, b))

