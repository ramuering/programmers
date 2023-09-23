import sys
n = list(sys.stdin.readline().strip())
tmp = []
for i in range(len(n)):
    tmp.append(''.join(n[i:]))
ans = sorted(tmp)
for a in ans:
    print(a)
