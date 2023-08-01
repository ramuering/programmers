graph=[]
for i in range(8):
  graph.append(list(input()))
  
cnt=0
for i in range(8):
  for j in range(8):
    if (i+j)%2==0:
      if graph[i][j]=='F':
        cnt+=1
    else:
      continue
print(cnt)