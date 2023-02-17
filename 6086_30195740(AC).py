a = int(input())
initial = 0
for i in range(1, a+1):
    initial += i
    if initial >= a:
        print(initial)
        break
