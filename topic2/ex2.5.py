a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and c + b > a:
    print('Треугольник существует')
else:
    print('Такой треугольник не может существовать')
