a, b, c = int(input()), int(input()), int(input())

if a == b and a != c:
    print('YES')
elif a == c and a != b:
    print('YES')
elif b == c and b != a:
    print('YES')
else:
    print('NO')            