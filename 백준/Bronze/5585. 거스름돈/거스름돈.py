import sys
n = int(sys.stdin.readline())
n = 1000-n
ans = 0
chk = [500, 100, 50, 10, 5, 1]
for i in range(6):
    while n >= chk[i]:
        n -= chk[i]
        ans += 1
print(ans)
