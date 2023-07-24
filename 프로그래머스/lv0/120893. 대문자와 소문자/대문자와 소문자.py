def solution(my_string):
    ans=[]
    for i in range(len(my_string)):
        if my_string[i].islower():
            ans.append(my_string[i].upper())
        else:
            ans.append(my_string[i].lower())
    return ''.join(ans)