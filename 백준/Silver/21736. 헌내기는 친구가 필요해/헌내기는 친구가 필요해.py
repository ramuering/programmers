from sys import stdin
from collections import deque


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 'X':
                continue
            if not vis[nx][ny]:
                vis[nx][ny] = True
                if graph[nx][ny] == 'P':
                    cnt += 1
                queue.append([nx, ny])


n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(n)]

vis = [[False]*m for _ in range(n)]
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x, y = i, j
            break

bfs(x, y)
if cnt == 0:
    print('TT')
else:
    print(cnt)
