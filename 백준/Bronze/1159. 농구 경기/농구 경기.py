n=int(input())
name={}
for i in range(n):
  a=input()
  if a[0] in name.keys():
    name[a[0]]+=1
  else:
    name[a[0]]=1
ans=[]
for n in name.keys():
  if name[n]>=5:
    ans.append(n)
if len(ans)==0:
  print('PREDAJA')
else:
  ans.sort()
  for i in ans:
    print(i,end='')