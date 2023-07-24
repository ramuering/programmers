def solution(my_string):
    dic={}
    answer=''
    for i in range(len(my_string)):
        key=my_string[i]
        if key not in dic.keys():
            dic[key]=1
            answer+=key
        else:
            continue
    return answer