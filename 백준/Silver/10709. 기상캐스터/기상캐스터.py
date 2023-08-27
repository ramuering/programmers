from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]

for i in range(n):
    chk = False
    for j in range(m):
        if graph[i][j] == 'c':
            chk = True
            cnt = 0
            print(cnt, end=' ')
        if not chk:
            print(-1, end=' ')
        if chk and graph[i][j] != 'c':
            cnt += 1
            print(cnt, end=' ')
    print()
