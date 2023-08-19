import sys
sys.setrecursionlimit(100000)

def bfs(x,y):
  if not vis[x][y]:
    vis[x][y]=True
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if rgb[nx][ny]==color:
          bfs(nx,ny)
  

n=int(input())
rgb=[list(input()) for _ in range(n)]

cnt1,cnt2=0,0
vis=[[False for _ in range(n)] for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
  
for i in range(n):
  for j in range(n):
    if vis[i][j]==False:
      color=rgb[i][j]
      bfs(i,j)
      cnt1+=1

for i in range(n):
  for j in range(n):
    if rgb[i][j]=='G':
      rgb[i][j]='R'

vis=[[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if vis[i][j]==False:
      color=rgb[i][j]
      bfs(i,j)
      cnt2+=1
      
print(cnt1,cnt2)