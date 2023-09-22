c = [0] * 10
n = 1
for i in range(0, 3):
    a = int(input())
    n *= a
for s in str(n):
    c[int(s)] += 1

for i in range(0, 10):
    print(c[i])
