def solution(numbers, k):
    ans=0
    for i in range(1,k):
        ans+=2
        if ans>=len(numbers):
            ans-=len(numbers)
    return numbers[ans]