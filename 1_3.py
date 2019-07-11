# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.


x1, y1 = map(float, input('Введите через пробел координаты первой точки: ').split())
x2, y2 = map(float, input('Введите через пробел координаты второй точки: ').split())

print('Уравнение прямой, которая проходит через заданные точки:')

if x1 == x2:
    print(f'x = {x1}')

else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    if b == 0:

        if k == 0:
            print('y = 0')

        else:
            print(f'y = {k}*x')

    else:
        if k == 0:
            print(f'y = {b}')

        else:
            print(f'y = {k}*x + {b}')