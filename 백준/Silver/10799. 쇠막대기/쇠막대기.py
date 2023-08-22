import sys

arr = list(sys.stdin.readline())

stack = 0
flag = False
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        flag = False
        stack += 1
    else:
        if stack > 0:
            if flag == False and arr[i-1] == '(':
                flag = True
                stack -= 1
                cnt += stack
            elif flag == True:
                stack -= 1
                cnt += 1
print(cnt)
