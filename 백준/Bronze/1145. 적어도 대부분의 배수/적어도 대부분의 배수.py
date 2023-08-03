nums=list(map(int,input().split()))
cnt=0
i=1
while True:
  for num in nums:
    if i%num==0:
      cnt+=1
  if cnt>=3:
    break
  cnt=0
  i+=1
print(i)
  
  