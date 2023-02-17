a, b, c = map(int, input().split())
minimum = a
minimum = minimum if minimum < b else b
minimum = minimum if minimum < c else c
print(minimum)
