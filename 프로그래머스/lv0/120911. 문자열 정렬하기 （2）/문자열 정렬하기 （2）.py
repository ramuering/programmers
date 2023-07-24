def solution(my_string):
    answer = ''
    my_string=my_string.lower()
    ans=sorted(list(my_string))
    return ''.join(ans)