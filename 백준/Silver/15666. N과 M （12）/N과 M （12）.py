import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
temp = list(combinations_with_replacement(nums, m))
ans = []
for i in range(len(temp)):
    tmp = []
    for j in range(m):
        tmp.append(temp[i][j])
    tmp.sort()
    ans.append(tmp)

ans = set(tuple(x) for x in ans)
ans = [list(x) for x in ans]
ans.sort()
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=' ')
    print()
