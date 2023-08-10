import sys
input=sys.stdin.readline

def bst(tree,m):
  left,right=1,max(tree)
  ans=0
  while left<=right:
    mid=(left+right)//2
    tmp=0
    for t in tree:
      if t>=mid:
        tmp+=(t-mid)
    if tmp>=m:
      left=mid+1
      ans=mid
    else:
      right=mid-1
  return ans
      
n,m=map(int,input().split())
tree=list(map(int,input().split()))
if sum(tree)<=m:
  print(0)
else:
  print(bst(tree,m))