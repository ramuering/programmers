from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))


for i in sorted(list(set(combinations(nums, m)))):
    for j in i:
        print(j, end=' ')
    print()
