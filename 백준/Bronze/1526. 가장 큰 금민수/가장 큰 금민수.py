import sys

n = sys.stdin.readline()
if len(n) == 1:
    if int(n) >= 7:
        print(7)
    else:
        print(4)
else:
    for i in range(int(n), 3, -1):
        i = str(i)
        flag = True
        for j in i:
            if j != '4' and j != '7':
                flag = False
                break
        if flag:
            print(i)
            break
