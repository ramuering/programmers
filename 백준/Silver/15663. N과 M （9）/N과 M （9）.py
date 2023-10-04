from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))


for i in sorted(list(set(permutations(nums, m)))):
    for j in i:
        print(j, end=' ')
    print()
