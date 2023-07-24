def solution(i, j, k):
    arr=[str(i) for i in range(i,j+1)]
    arr=list(''.join(arr))
    
    answer=arr.count(str(k))
    return answer