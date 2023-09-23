a = [0] * 42

for i in range(0, 10):
    b = int(input())
    a[b % 42] += 1

result = 0

for i in a:
    if i > 0:
        result += 1

print(result)