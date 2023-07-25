def solution(s):
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)<=0:
                return False
            if stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    return True