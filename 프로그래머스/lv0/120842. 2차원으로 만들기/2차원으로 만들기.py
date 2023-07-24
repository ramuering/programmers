def solution(num_list, n):
    answer = []
    tmp=[]
    for i in range(1,len(num_list)+1):
        tmp.append(num_list[i-1])
        if i%n==0:
            answer.append(tmp)
            tmp=[]
    return answer