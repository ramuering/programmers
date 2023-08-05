t=int(input())

for _ in range(t):
  n,m=map(int,input().split())
  prior=list(map(int,input().split()))
  tmp=[i for i in range(len(prior))]
  cnt=0
  while True:
    if prior[0]>=max(prior):
      cnt+=1
      if tmp[0]==m:
        break
      else:
        prior=prior[1:]
        tmp=tmp[1:]
    else:
      prior=prior[1:]+prior[:1]
      tmp=tmp[1:]+tmp[:1]
  print(cnt)
