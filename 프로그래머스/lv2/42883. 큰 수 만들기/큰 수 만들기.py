def solution(chk, k):
    chk=list(int(x) for x in chk)
    stack=[]
    for i in range(len(chk)):
        if len(stack)==0:
            stack.append(chk[i])
            continue
        if k > 0:
            while stack[-1]<chk[i]:
                stack.pop()
                k-=1
                if len(stack)==0 or k<=0:
                    break
        stack.append(chk[i])
    stack=list(str(x) for x in stack)
    if k>0:
        stack=stack[:-k]
    return ''.join(stack)
    