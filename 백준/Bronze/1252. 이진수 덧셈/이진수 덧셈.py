n, m = map(int, input().split())
n = int('0b'+str(n), 2)
m = int('0b'+str(m), 2)
print(format(n+m, 'b'))
