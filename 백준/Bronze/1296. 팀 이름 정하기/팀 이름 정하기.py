name = list(input())
L = name.count('L')
O = name.count('O')
V = name.count('V')
E = name.count('E')
n = int(input())
team = []
cnt = []
max_cnt = -1
for i in range(n):
    team.append(input())
team.sort()
for i in range(n):
    L2 = L+team[i].count('L')
    O2 = O+team[i].count('O')
    V2 = V+team[i].count('V')
    E2 = E+team[i].count('E')
    tmp = ((L2+O2)*(L2+V2)*(L2+E2)*(O2+V2)*(O2+E2)*(V2+E2)) % 100
    if tmp > max_cnt:
        max_cnt = tmp
        ans = team[i]
    else:
        continue

print(ans)
