def solution(n):
    ans=[i for i in range(1,n+1) if i%2==0]
    return sum(ans)