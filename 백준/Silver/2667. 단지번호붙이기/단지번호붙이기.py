import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
  global cnt
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False
  else:
    if graph[x][y]==1:
      graph[x][y]=0
      cnt+=1
      dfs(x-1,y)
      dfs(x+1,y)
      dfs(x,y-1)
      dfs(x,y+1)
      return True
  return False

n=int(input())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

cnt=0
ans=[]
for i in range(n):
  for j in range(n):
    if dfs(i,j):
        ans.append(cnt)
        cnt=0
print(len(ans))
ans.sort()
for i in range(len(ans)):
  print(ans[i])
