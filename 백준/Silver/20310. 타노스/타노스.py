import sys
from itertools import permutations
s = sys.stdin.readline()
zero = ['0']*(s.count('0')//2)
one = ['1']*(s.count('1')//2)
ans = zero+one
print(''.join(ans))
