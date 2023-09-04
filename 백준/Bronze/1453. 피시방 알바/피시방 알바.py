n = int(input())
arr = [False]*100
nrr = list(map(int, input().split()))
ans = 0
for i in nrr:
    if arr[i-1]:
        ans += 1
    else:
        arr[i-1] = True

print(ans)
