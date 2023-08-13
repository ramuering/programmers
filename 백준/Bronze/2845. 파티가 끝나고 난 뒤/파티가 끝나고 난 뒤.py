a,b=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    print(arr[i]-(a*b),end=' ')