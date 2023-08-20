import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline().strip()) for _ in range(n)]
rope.sort()
ans = 0

for i in range(1, n + 1):
    ans = max(ans, (n - i + 1) * rope[i-1])


print(ans)
