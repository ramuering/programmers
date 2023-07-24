def solution(n):
    ans = []
    i=1
    while True:
        i+=1
        if n%i==0:
            ans.append(i)
            n=n//i
            i=1
        if n==1:
            break
    ans=list(set(ans))
    ans.sort()
    return ans