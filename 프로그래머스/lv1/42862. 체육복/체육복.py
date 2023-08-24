def solution(n, lost, reserve):
    num={i:1 for i in range(n+2)}
    for i in range(1,n+1):
        if i in lost:
            num[i]-=1
        if i in reserve:
            num[i]+=1
    ans = 0
    for i in range(1,n+1):
        if num[i]==0:
            if num[i-1]==2:
                num[i-1]=1
                num[i]+=1
            elif num[i+1]==2:
                num[i+1]=1
                num[i]+=1
        if num[i]==1 or num[i]==2:
            ans+=1
    return ans
        
                
            