cnt = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt += 1
    name = []
    for i in range(n):
        name.append(input())
    tmp = []
    for i in range(2*n-1):
        a, b = input().split()
        tmp.append(int(a))
    check = 0
    for i in range(1, n+1):
        if tmp.count(i) == 1:
            check = i
            break
    print(cnt, name[check-1])
