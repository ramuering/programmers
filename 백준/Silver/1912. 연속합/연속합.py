import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
dp=[0]*n

dp[0]=nums[0]
if n==1:
  print(dp[0])
else:
  for i in range(1,n):
    # 해당 수가 음수일 경우
    if dp[i-1]<0:
      dp[i]=nums[i]
    else:
      dp[i]=dp[i-1]+nums[i]
  print(max(dp))