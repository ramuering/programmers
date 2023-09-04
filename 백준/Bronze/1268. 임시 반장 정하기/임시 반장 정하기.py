from sys import stdin
n = int(stdin.readline())
stu = [list(map(int, stdin.readline().split())) for _ in range(n)]
chk = [[] for _ in range(n)]
for j in range(5):
    tmp = []
    for i in range(n):
        tmp.append(stu[i][j])
    for t in range(n):
        if tmp.count(tmp[t]) > 1:
            for i in range(n):
                if tmp[t] == tmp[i] and i != t:
                    chk[t].append(i)

chk = [set(chk[x]) for x in range(n)]
ans = -1
mlen = -1
for i in range(n):
    if mlen < len(chk[i]):
        ans = i
        mlen = len(chk[i])

print(ans+1)
