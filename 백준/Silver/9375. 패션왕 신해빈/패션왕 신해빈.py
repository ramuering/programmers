import sys
from math import comb


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        a, b = sys.stdin.readline().strip().split()
        if b in clothes.keys():
            clothes[b].append(a)
        else:
            clothes[b] = [a]
    ans = 1
    for i in range(len(list(clothes.values()))):
        ans *= len(list(clothes.values())[i])+1
    print(ans-1)
