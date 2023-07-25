from collections import deque
def solution(progresses, speeds):
    answer=[]
    queue=deque([i for i in progresses])
    speeds=deque(speeds)
    while queue:
        cnt=0
        for i in range(len(queue)):
            queue[i]+=speeds[i]
        print(queue)
        while queue and queue[0]>=100:
                queue.popleft()
                speeds.popleft()
                cnt+=1
        if cnt!=0:
            answer.append(cnt)    
    return answer