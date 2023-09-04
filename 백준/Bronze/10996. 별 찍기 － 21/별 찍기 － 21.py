import math

n = int(input())
a = math.ceil(n/2)
b = a
if n % 2 != 0:
    b -= 1

for i in range(n*2):
    if i % 2 == 0:
        for _ in range(a):
            print('*', end=' ')
    else:
        for _ in range(b):
            print(' *', end='')
    print()
