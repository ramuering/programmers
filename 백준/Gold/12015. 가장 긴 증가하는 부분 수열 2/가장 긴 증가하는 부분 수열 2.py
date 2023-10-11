import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

stack = []
for num in nums:
    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
    else:
        i = bisect_left(stack, num)
        stack[i] = num
print(len(stack))
