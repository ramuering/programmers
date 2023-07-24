def solution(age):
    age=list(str(age))
    answer=''
    for i in range(len(age)):
        answer+=chr(int(age[i])+97)
    return answer