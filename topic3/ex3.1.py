n = int(input())
count = 0 
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        count += 1
print(count)        