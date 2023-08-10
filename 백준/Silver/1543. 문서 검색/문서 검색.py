s=input()
chk=input()

ans=0
start=0
while True:
  idx=s.find(chk,start)
  if idx==-1:
    break
  else:
    if chk in s[start:]:
      ans+=1
      start=idx+len(chk)
print(ans)
