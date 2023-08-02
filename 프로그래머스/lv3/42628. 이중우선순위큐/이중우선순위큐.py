from heapq import heappush
from heapq import nlargest
from heapq import nsmallest

def solution(oper):
    heap = []
    for i in range(len(oper)):
        a,b=oper[i].split()
        if a=='I':
            heappush(heap,int(b))
        elif a=='D':
            if b=='-1':
                heap=nlargest(len(heap)-1,heap)
            elif b=='1':
                heap=nsmallest(len(heap)-1,heap)
    if len(heap)==0:
        return [0,0]
    return max(heap),min(heap)
