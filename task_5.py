# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.


a, b = input('Введите через пробел 2 строчные латинские буквы: ').split()

num_a = ord(a) - 96
num_b = ord(b) - 96

distance = abs(num_b - num_a - 1)

print(f'Позиции введенных букв в алфавите: {num_a} и {num_b}')
print(f'Между этими буквами букв: {distance}')