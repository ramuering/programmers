from itertools import permutations

n, r = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for numbers in permutations(nums, r):
    for num in numbers:
        print(num, end=' ')
    print()
