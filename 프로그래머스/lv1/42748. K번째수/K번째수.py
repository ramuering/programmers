def solution(array, commands):
        ans=[]
        for i in range(len(commands)):
            chk=sorted(array[commands[i][0]-1:commands[i][1]])
            ans.append(chk[commands[i][2]-1])            
        return ans