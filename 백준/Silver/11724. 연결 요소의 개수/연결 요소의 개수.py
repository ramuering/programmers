import sys
sys.setrecursionlimit(100000)

def dfs(graph,x):
  vis[x]=True
  for i in graph[x]:
    if vis[i]==False:
      dfs(graph,i)

n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
vis=[False]*(n+1)

for i in range(m):
  x,y=map(int,sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
  
ans=0 

for i in range(1,n+1):
  if vis[i]==False:
    dfs(graph,i)
    ans+=1
print(ans)