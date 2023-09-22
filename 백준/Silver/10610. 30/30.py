from sys import stdin


n = list(stdin.readline().strip())

if '0' not in n:
    print(-1)
else:
    tmp = 0
    for i in range(len(n)):
        tmp += int(n[i])
    if tmp % 3 != 0:
        print(-1)
    else:
        n = sorted(n, reverse=True)
        ans = ''.join(n)
        print(ans)
