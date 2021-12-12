import random

n = 10
a = [0] * n

for x in range(n):
    a[x] = [0] * n
    for i in range(n):
        a[x][i] = random.randint(1, 100)
"""
for x in range(n):
    print("{")
    for i in range(n):
        print(str(a[x][i]) + ",", end="")
    print("},", end="")
"""
print(a)
