from sys import stdin
from heapq import heapify, heappop, heappush

t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    file = list(map(int, stdin.readline().split()))
    heapify(file)
    ans = 0

    while len(file) >= 2:
        a = heappop(file)
        b = heappop(file)
        ans += (a+b)
        heappush(file, (a+b))
    print(ans)
