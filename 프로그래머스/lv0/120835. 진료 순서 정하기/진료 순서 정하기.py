def solution(emergency):
    chk=emergency[:]
    emergency.sort(reverse=True)
    answer = {}
    ans=[]
    for i in range(len(emergency)):
        answer[emergency[i]]=i+1
    answer= dict(sorted(answer.items()))
    for i in chk:
         ans.append(answer[i])
    return ans