k = int(input())
a, b = 1, 0
for i in range(k):
    tmpa, tmpb = 0, 0
    if a > 0:
        tmpb = a
        a = 0
    if b > 0:
        tmpa = b
        tmpb += b
    a, b = tmpa, tmpb
print(a, b)
