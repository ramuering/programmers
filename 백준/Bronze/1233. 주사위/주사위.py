from itertools import product

dice={}
arr=list(map(int,input().split()))
a=[i for i in range(1,arr[0]+1)]
b=[i for i in range(1,arr[1]+1)]
c=[i for i in range(1,arr[2]+1)]
for i in list(product(a,b,c)):
  if sum(i) in dice.keys():
    dice[sum(i)]+=1
  else:
    dice[sum(i)]=1
tmp=0
ans=-1
for i in dice.keys():
  if tmp < dice[i]:
    ans=i
    tmp=dice[i]
  elif tmp==dice[i]:
    ans=min(ans,i)
  else:
    continue
  
print(ans)
