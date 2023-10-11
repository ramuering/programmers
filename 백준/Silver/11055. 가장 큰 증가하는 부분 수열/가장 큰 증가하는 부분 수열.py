import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0]*n
dp[0] = nums[0]
ans = dp[0]
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += nums[i]
    ans = max(ans, dp[i])
print(ans)
