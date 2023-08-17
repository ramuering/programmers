num=list(input())
dp=[0]*(len(num))
dp[0]=1
if num[0]=='0':
  print(0)
else:
  for i in range(1,len(num)):
    if int(num[i-1]+num[i])==0:
      print(0)
      exit(0)
    if 1<=int(num[i])<=9:
      dp[i]=dp[i-1]
    if 10<=int(num[i-1]+num[i])<=26:
      if i==1:
        dp[i]+=1
      else:
        dp[i]+=dp[i-2]
  print(dp[-1]%1000000)
      
      
