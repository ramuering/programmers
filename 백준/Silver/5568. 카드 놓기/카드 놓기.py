import sys
from itertools import permutations
from math import comb
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
nums = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set(''.join(i) for i in permutations(nums, k))))
