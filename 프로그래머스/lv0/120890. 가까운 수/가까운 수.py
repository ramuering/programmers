def solution(array, n):
    answer=0
    m=100
    for i in range(len(array)):
        chk=abs(n-array[i])
        if m>chk:
            m=chk
            answer=array[i]
        elif m==chk:
            answer=min(answer,array[i])
    return answer