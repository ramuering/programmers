from heapq import heappush,heappop
import sys
n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
  num=int(sys.stdin.readline())
  if num==0:
    if len(heap)==0:
      print(0)
    else:
      print(heappop(heap)[1])
  else:
    heappush(heap,(-num,num))
    