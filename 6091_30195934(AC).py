a, b, c = map(int,input().split())
# 최소공배수를 구해라
for i in range(1, a*b+1):
    if (b * i) % a == 0:
        LCM = b * i
        break
for i in range(1, LCM * c+1):
    if (LCM * i) % c == 0:
        LCM = LCM * i
        break
print(LCM)
