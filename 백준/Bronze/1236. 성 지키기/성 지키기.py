from sys import stdin
n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]
tmp1, tmp2 = 0, 0
for i in range(n):
    if 'X' not in graph[i]:
        tmp1 += 1
for j in range(m):
    chk = False
    for i in range(n):
        if graph[i][j] == 'X':
            chk = True
    if not chk:
        tmp2 += 1

print(max(tmp1, tmp2))
