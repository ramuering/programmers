def solution(order):
    ans=0
    order=list(str(order))
    for i in ('3','6','9'):
        ans+=order.count(i)
    return ans