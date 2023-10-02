import sys
sys.setrecursionlimit(100000)


def dfs(x):
    for i in graph[x]:
        if vis[i] == 0:
            vis[i] = x
            dfs(i)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [0]*(n+1)

dfs(1)

for i in range(2, n+1):
    print(vis[i])
