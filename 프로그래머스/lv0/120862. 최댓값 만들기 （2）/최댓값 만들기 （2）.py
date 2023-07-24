from itertools import combinations
def solution(numbers):
    numbers.sort(key=lambda x : abs(x))
    max=-100000000
    for i in combinations(numbers,2):
        tmp=i[0]*i[1]
        if max<tmp:
            max=tmp
    return max