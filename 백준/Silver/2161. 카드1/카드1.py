n=int(input())
card=[i for i in range(1,n+1)]
dump=[]


while len(card)>1:
  tmp=card.pop(0)
  dump.append(tmp)
  tmp=card.pop(0)
  card.append(tmp)

for d in dump:
  print(d,end=' ')
print(card[0])