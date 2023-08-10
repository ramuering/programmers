n=int(input())
tmp=[int(input()) for _ in range(n)]
nums={}

for num in tmp:
  if num in nums.keys():
    nums[num]+=1
  else:
    nums[num]=1

arr=[i*nums[i] for i in nums.keys()]
print(round(sum(arr)/n))
print(sorted(tmp)[int(n/2)])
max_v=max(nums.values())
max_k=[k for k,v in nums.items() if v==max_v]
if len(max_k)>1:
  keys=sorted(max_k)
  print(keys[1])
else:
  print(max_k[0])
print(max(nums.keys())-min(nums.keys()))  

