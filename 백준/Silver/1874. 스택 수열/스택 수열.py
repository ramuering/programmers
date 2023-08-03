from sys import stdin

n=int(stdin.readline())
ans=[]
stack=[]
cnt=1
for i in range(n):
  num=int(stdin.readline())
  while cnt<=num:
    stack.append(cnt)
    ans.append('+')
    cnt+=1
  if stack[-1]==num:
    stack.pop()
    ans.append('-')
  else:
    print("NO")
    exit(0)
for i in ans:
  print(i)

    

