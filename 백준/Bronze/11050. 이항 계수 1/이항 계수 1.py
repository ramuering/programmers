n, m = map(int, input().split())


def binomial(n, m):
    if (m == 0 or n == m):
        return 1
    else:
        return binomial(n-1, m-1) + binomial(n-1, m)


print(binomial(n, m))
