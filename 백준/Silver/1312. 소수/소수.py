from sys import stdin

a, b, n = map(int, stdin.readline().split())

for i in range(n):
  a=(a%b)*10
  ans=a//b
print(ans)