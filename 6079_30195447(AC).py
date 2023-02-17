a = int(input())
b = 0
for i in range(a):
    b += i
    if b >= a:
        print(i)
        break
