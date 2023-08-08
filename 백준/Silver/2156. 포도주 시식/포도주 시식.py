n=int(input())
cup=[]
dp=[0]*n
for _ in range(n):
  cup.append(int(input()))
  
if n==1:
  print(cup[0])
elif n==2:
  print(sum(cup))
else:   
  dp[0]=cup[0]
  dp[1]=cup[0]+cup[1]
  dp[2]=max(cup[0],cup[1])+cup[2]

  for i in range(3,n):
    dp[i]=max(dp[i-4]+cup[i-1]+cup[i],dp[i-2]+cup[i],dp[i-3]+cup[i-1]+cup[i])

  print(max(dp))