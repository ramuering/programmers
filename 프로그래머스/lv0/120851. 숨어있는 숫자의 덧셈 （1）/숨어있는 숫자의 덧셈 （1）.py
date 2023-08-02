def solution(my_string):
    ans=0
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            ans+=int(my_string[i])
    return ans