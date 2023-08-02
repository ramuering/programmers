n,k=map(int,input().split())
nums=[i for i in range(1,n+1)]
ans=[]
i=0
while True:
  i=(i+(k-1))%len(nums)
  ans.append(nums[i])
  del nums[i]
  if len(nums)==0:
    break 
print("<",end='') 
for i in range(len(ans)):
  if ans[i]==ans[-1]:
    print(ans[i],end='')
    print(">")
  else:
    print(ans[i],end='')
    print(",",end=' ')