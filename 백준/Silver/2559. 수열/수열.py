n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_tmp, end, tmp = -10000000, 0, 0
for start in range(n):
    cnt = 0
    while end-start < k and end < n:
        tmp += nums[end]
        end += 1
        cnt += 1
    if max_tmp < tmp:
        max_tmp = tmp
    if start+k >= n:
        break
    tmp -= nums[start]
print(max_tmp)
