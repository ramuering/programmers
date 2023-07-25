t=int(input())
dp=[0]*41
dp[0]=[1,0]
dp[1]=[0,1]

for i in range(t):
  n=int(input())
  for j in range(n+1):
    if dp[j]==0:
      a=dp[j-1][0]+dp[j-2][0]
      b=dp[j-1][1]+dp[j-2][1]
      dp[j]=[a,b]
    else:
      continue
  print(dp[n][0],dp[n][1])