n = int(input())

for i in range(0, n):
    arr = list(map(str, input().split("X")))
    sum = 0
    for s in arr:
        if not s == '':
            for i in range(1, len(s) + 1):
                sum += i
    print(sum)