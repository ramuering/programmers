import sys

t=int(sys.stdin.readline())
cost=[]
dp=[[0,0,0] for _ in range(t)]
for i in range(t):
  cost.append(list(map(int,sys.stdin.readline().split())))
dp[0]=cost[0]       
for i in range(1,t):
  dp[i][0]=min(dp[i-1][1]+cost[i][0],dp[i-1][2]+cost[i][0])
  dp[i][1]=min(dp[i-1][0]+cost[i][1],dp[i-1][2]+cost[i][1])
  dp[i][2]=min(dp[i-1][0]+cost[i][2],dp[i-1][1]+cost[i][2])
print(min(dp[t-1]))