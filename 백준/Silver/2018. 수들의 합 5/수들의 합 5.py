n = int(input())
nums = [i for i in range(1, n+1)]

cnt = 0
end = 0
tmp = 0
for start in range(n):
    while tmp < n and end < n:
        tmp += nums[end]
        end += 1
    if tmp == n:
        cnt += 1
    tmp -= nums[start]
print(cnt)
