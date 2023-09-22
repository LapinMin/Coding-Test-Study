n = int(input())

for i in range(0, n):
    a, b = map(str, input().split())
    print(''.join([s * int(a) for s in b]))
