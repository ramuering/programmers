def solution(my_string):
    arr=my_string.split()
    ans=int(arr[0])
    sign=''
    for i in range(1,len(arr)):
        if arr[i].isdigit():
            if sign=='+':
                ans+=int(arr[i])
            else:
                ans-=int(arr[i])
        else:
            if arr[i]=='+':
                sign='+'
            else:
                sign='-'
    return ans