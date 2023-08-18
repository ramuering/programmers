N,m,M,T,R=map(int,input().split())
cnt,n=0,0
x=m
if x+T > M:
  print(-1)
else:
  while True:
    cnt+=1
    if x+T<=M:
      x+=T
      n+=1
      if n==N:
        break
    else:
      if x-R<m:
        x=m
      else:
        x-=R

  print(cnt)
    