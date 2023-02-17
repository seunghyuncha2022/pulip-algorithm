n = int(input())
a = input().split()
# a에 1~23에 중복되서 불린 숫자 수를 구하자
for i in range(n):
    a[i] = int(a[i]) # a에 있는 str -> int
d = []
for i in range(24):
    d.append(0)
for i in range(n):
    d[a[i]] += 1
for i in range(1, 24):
    print(d[i], end = ' ')
