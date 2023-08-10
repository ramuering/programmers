n=int(input())
room=[input() for _ in range(n)]
roomA=[]
for i in range(n):
  tmp=''
  for j in range(n):
    tmp+=room[j][i]
  roomA.append(tmp.split('X'))
room=[x.split('X') for x in room]

a,b=0,0
for i in range(n):
  for j in range(len(room[i])):
    if '..' in room[i][j]:
      a+=1
  for j in range(len(roomA[i])):
    if '..' in roomA[i][j]:
      b+=1
print(a,b)

  