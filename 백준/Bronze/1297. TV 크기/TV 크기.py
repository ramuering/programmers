d, H, W = map(int, input().split())
r = d/(H**2+W**2)**0.5
print(int(H*r), int(W*r))
