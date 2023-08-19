def solution(answer):
    p=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    ans=[0,0,0]
    for i in range(len(answer)):
        if p[0][i%len(p[0])]==answer[i]:
            ans[0]+=1
        if p[1][i%len(p[1])]==answer[i]:
            ans[1]+=1
        if p[2][i%len(p[2])]==answer[i]:
            ans[2]+=1
    m=0
    answer=[]
    for i in range(3):
        if ans[i]>m:
            answer=[i+1]
            m=ans[i]
        elif ans[i]==m:
            answer.append(i+1)
    answer.sort()
    return answer