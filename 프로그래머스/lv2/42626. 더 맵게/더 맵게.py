import heapq

def solution(scoville, k):
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    cnt=0
    while True:
        if len(heap)==1:
            if heap[0]<k:
                return -1
        if heap[0]>=k:
            return cnt
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap,a+(b*2))
        cnt+=1