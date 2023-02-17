n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i]) # a에 있는 str -> int
for i in range(n-1,-1,-1):
    print(a[i], end=' ')
