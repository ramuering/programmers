from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in list(combinations_with_replacement(nums, m)):
    for j in i:
        print(j, end=' ')
    print()
