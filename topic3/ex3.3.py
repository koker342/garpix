lst = [10, 17, 13, 44, 23, 88, 100, 99]
for i in lst:
    if i % 2 == 0:
        print(i, end=' ')
else:
    print("- четные числа")        
for i in lst:
    if i % 2 != 0:
        print(i, end=' ')
else:
    print("- нечетные числа")        
