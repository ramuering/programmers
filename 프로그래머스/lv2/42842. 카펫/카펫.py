def solution(brown, yellow):
    tmp=brown+yellow
    for i in range(1,tmp):
        if tmp%i==0:
            j=tmp//i
            if brown==(i*2)+((j-2)*2):
                return [j,i]