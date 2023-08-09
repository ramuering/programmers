e,s,m=map(int,input().split())
a,b,c=1,1,1
ans=1
if e==1 and s==1 and m==1:
  print(ans)
else:
  while True:
    ans+=1
    a=(a+1)%15
    if a==0:
      a=15
    b=(b+1)%28
    if b==0:
      b=28
    c=(c+1)%19
    if c==0:
      c=19
    if a==e and b==s and c==m:
      break
  print(ans)