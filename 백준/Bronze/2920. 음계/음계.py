arr = list(map(int, input().split()))
chk = sorted(arr)
chk_r = sorted(arr, reverse=True)
if chk == arr:
    print('ascending')
elif chk_r == arr:
    print('descending')
else:
    print('mixed')
