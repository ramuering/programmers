def solution(cit):
    cit.sort()
    ans=0
    for i in range(max(cit),-1,-1):
        tmp=[x for x in cit if x >=i]
        if len(tmp)>=i:
            ans=max(i,ans)
    return ans
                
                