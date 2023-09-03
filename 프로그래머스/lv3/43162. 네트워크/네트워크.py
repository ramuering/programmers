
def solution(n, com):
    cnt=0
    vis= [False for i in range(n)]
    def dfs(x):
        vis[x]=True
        for i in range(n):
            if com[x][i]==1 and not vis[i]:
                dfs(i)
        
    for i in range(n):
        if not vis[i]:
            dfs(i)
            cnt+=1
    return cnt
                