﻿r, g, b = map(int,input().split())
iteration = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            iteration += 1
            print(i,j,k)
print(iteration)
