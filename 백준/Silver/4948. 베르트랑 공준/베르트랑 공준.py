import sys


nums = [True for _ in range(246913)]

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    for i in range(2, (2*n)+1):
        if nums[i] == True:
            j = 2
            while i*j <= 2*n:
                nums[i*j] = False
                j += 1
    print(nums[n+1:(2*n)+1].count(True))
