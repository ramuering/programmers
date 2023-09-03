cnt=0
def solution(numbers, target):
    global cnt
    ans=0
    def dfs(i, ans):
        global cnt
        if i==len(numbers):
            if ans==target:
                cnt+=1
        else:
            dfs(i+1,ans+numbers[i])
            dfs(i+1,ans-numbers[i])
    dfs(0,ans)
    return cnt