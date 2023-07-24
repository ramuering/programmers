def solution(s):
    ans=[]
    tmp=set(list(s))
    s=list(s)
    print(tmp)
    print(s)
    for i in tmp:
        if s.count(i)==1:
            ans.append(i)
    ans.sort()
    return ''.join(ans)