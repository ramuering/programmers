def solution(board, moves):
    cnt=0
    stack=[]
    for i in moves:
        for j in range(len(board)):
            chk=board[j][i-1]
            board[j][i-1]=0
            if chk!=0:
                if len(stack)==0:
                    stack.append(chk)
                    break
                if len(stack)>0:
                    if stack[-1]==chk:
                        stack.pop()
                        cnt+=2
                        break
                    else:
                        stack.append(chk)
                        break
    return cnt