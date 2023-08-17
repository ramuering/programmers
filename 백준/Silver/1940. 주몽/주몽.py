n=int(input())
m=int(input())
arr=list(map(int,input().split()))
vis=[False]*n
cnt=0

for i in range(n-1):
  for j in range(i+1,len(arr)):
    if (arr[i]+arr[j])==m and vis[i]==False and vis[j]==False:
      vis[i],vis[j]=True, True
      cnt+=1
print(cnt)
  
