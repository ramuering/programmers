n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in range(n):
  ma=a.index(max(a))
  nb=b.index(min(b))
  s+=a[ma]*b[nb]
  del a[ma]
  del b[nb]

print(s)  
  