n, m = map(int, input().split())
nums = list(map(int, input().split()))

tmp_sum, end, cnt = 0, 0, 0
for start in range(n):
    while tmp_sum < m and end < n:
        tmp_sum += nums[end]
        end += 1
    if tmp_sum == m:
        cnt += 1
    tmp_sum -= nums[start]
print(cnt)
