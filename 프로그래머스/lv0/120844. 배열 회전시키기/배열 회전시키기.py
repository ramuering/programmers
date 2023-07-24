def solution(numbers, direction):
    ans=[]
    if direction=='left':
        ans=numbers[1:]
        ans.append(numbers[0])
    else:
        ans=numbers[:-1]
        ans.insert(0,numbers[-1])
            
            
    return ans