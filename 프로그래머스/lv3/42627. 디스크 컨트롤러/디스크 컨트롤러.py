from heapq import heappush, heappop

def solution(jobs):
    heap=[]
    s,e=-1,0
    cnt=0
    ans=0
    while len(jobs)>cnt:
        for j in jobs:
            if s<j[0]<=e:
                heappush(heap,(j[1],j[0]))
        if len(heap)>0:
            temp=heappop(heap)
            s=e
            e+=temp[0]
            ans+=(e-temp[1])
            cnt+=1
        else:
            e+=1
    return ans//len(jobs)
            
            
    
        
        