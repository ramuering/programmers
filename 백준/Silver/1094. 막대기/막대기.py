x=int(input())
tmp=[64]
if x==64:
  print(1)
else:
  while True:
    tmp.sort(reverse=True)
    temp=(tmp.pop())//2
    tmp.append(temp)
    if sum(tmp)<x:
      tmp.append(temp)
    if sum(tmp)==x:
      print(len(tmp))
      break