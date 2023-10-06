from itertools import product

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

for i in product(nums, repeat=m):
    for j in i:
        print(j, end=' ')
    print()

    