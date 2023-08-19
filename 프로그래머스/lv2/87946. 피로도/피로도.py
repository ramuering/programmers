from itertools import permutations

def solution(k, dung):
    tmp=[i for i in range(len(dung))]
    ans=0
    for arr in list(permutations(tmp,len(tmp))):
        x=k
        cnt=0
        for i in arr:
            if x>= dung[i][0]:
                cnt+=1
                x-=dung[i][1]
        if ans<cnt:
            ans=cnt
    return ans