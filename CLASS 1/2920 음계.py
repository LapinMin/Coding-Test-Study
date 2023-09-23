a = list(map(int, input().split()))
b = a.copy()
c = sorted(a)
if b[0] == 1:
    if b == c:
        print("ascending")
    else:
        print("mixed")
elif b[0] == 8:
    c.sort(reverse=True)
    if b == c:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")