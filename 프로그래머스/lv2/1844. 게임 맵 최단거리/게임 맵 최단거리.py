from collections import deque

def solution(maps):

    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    
    def bfs(x,y):
        queue=deque()
        queue.append([x,y])
        
        while queue:
            x,y=queue.popleft()
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx >= len(maps) or nx < 0 or ny >= len(maps[0]) or ny < 0:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    queue.append([nx, ny])
        return maps[len(maps)-1][len(maps[0])-1]

    ans=bfs(0,0)
    if ans==1:
        return -1
    else:
        return ans
            