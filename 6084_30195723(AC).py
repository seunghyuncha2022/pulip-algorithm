h, b, c, s = map(int,input().split())
result = h*b*c*s/(8*1024**2)
print(format(result,'.1f'),'MB')
