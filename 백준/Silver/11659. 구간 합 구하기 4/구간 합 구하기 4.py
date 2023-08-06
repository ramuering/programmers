import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

result = [0]*100005
for i in range(len(arr)):
    result[i+1] = arr[i]+result[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(result[j]-result[i-1])
