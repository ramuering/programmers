from itertools import combinations_with_replacement

n,m=map(int,input().split())

nums=[i for i in range(1,n+1)]
for i in list(combinations_with_replacement(nums,m)):
  for j in range(len(i)):
    print(i[j],end=' ')
  print()
