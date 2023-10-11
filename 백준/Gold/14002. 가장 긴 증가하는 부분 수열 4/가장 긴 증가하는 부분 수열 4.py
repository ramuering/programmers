import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

ans = [[] for _ in range(n)]

dp = [1]*n
result = -1
tmp = -1
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                if len(ans[j]) > len(ans[i]):
                    ans[i] = ans[j][:]
                else:
                    ans[i].append(nums[j])
            else:
                continue
    ans[i].append(nums[i])
    if dp[i] > result:
        result = dp[i]
        tmp = i
print(result)
for i in range(len(ans[tmp])):
    if i == len(ans[tmp])-1:
        print(ans[tmp][i])
    else:
        print(ans[tmp][i], end=' ')

