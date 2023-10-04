from itertools import product

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))


for num in list(product(nums, repeat=m)):
    for i in num:
        print(i, end=' ')
    print()
