import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
while n > 0:
    n -= 1
    chk = list(sys.stdin.readline().split())
    if chk[0] == 'push':
        queue.append(chk[1])
    elif chk[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif chk[0] == 'size':
        print(len(queue))
    elif chk[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif chk[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif chk[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
