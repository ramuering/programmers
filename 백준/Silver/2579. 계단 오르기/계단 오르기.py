import sys

n=int(sys.stdin.readline())
a=[]
for i in range(n):
  a.append(int(sys.stdin.readline()))
dp=[0]*n
if n<=2:
  print(sum(a))
else:
  dp[0]=a[0]
  dp[1]=a[0]+a[1]
  dp[2]=max(a[0],a[1])+a[2]

  for i in range(3,n):
    dp[i]=max(dp[i-2],dp[i-3]+a[i-1])+a[i]
  
  print(dp[-1])
