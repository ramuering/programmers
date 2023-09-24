import sys
n, k = map(int, sys.stdin.readline().strip().split())
nums = [True for _ in range(n+1)]
cnt = 0
ans = False
for i in range(2, n+1):
    if nums[i] == True:
        j = 1
        while i*j <= n:
            if nums[i*j] == True:
                nums[i*j] = False
                cnt += 1
                if cnt == k:
                    ans = i*j
                    break
                j += 1
            else:
                j += 1
    if ans:
        print(ans)
        break
