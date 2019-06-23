import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if 'keys' in dir(var):

            for j in var:
                print(f'\nПодпеременная: \'{j}\' весит {sys.getsizeof(j)}')

                if '__iter__' in dir(var[j]):

                    if 'keys' in dir(var[j]):
                        spam += memory_count([var[j]]) + sys.getsizeof(j)

                    else:
                        spam += memory_count(var[j]) + sys.getsizeof(j) + sys.getsizeof(var[j])

                else:
                    print(f'Вес его значения {var[j]}: {sys.getsizeof(var[j])}')
                    spam += sys.getsizeof(var[j]) + sys.getsizeof(j)

        else:

            if '__iter__' in dir(var) and not isinstance(var, str):

                for j in var:
                    print(f'\nПодпеременная: {j} весит {sys.getsizeof(j)}')

                    if '__iter__' in dir(j):
                        spam += memory_count(j) + sys.getsizeof(j)

                    else:
                        spam += sys.getsizeof(j)

        memory += spam

    return memory


# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

a = int(input('Введите целое трехзначное число:'))

hundred = a // 100
dozen = (a // 10) % 10
unit = a % 10

summa = hundred + dozen + unit
mult = hundred * dozen * unit

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')




# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# summa = (a // 100) + ((a // 10) % 10) + (a % 10)
# mult = (a // 100) * ((a // 10) % 10) * (a % 10)
#
# print(f'Сумма цифр в числе: {summa}')
# print(f'Произведение цифр в числе: {mult}')





# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
# print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')



# ***************************************************************************************************
_variable = []
for i in dir():
    if i[0] != '_' and '__name__' not in dir(locals()[i]):
        _variable.append(locals()[i])

print('\nЗатраты памяти программы: ', memory_count(_variable))
print('\nПеременные: ', _variable)