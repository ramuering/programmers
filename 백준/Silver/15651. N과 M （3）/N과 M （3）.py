from itertools import product

n,m=map(int,input().split())

nums=[i for i in range(1,n+1)]
for i in list(product(nums,repeat=m)):
  for j in range(len(i)):
    print(i[j],end=' ')
  print()
