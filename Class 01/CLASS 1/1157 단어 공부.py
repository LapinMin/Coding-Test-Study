w = input().upper()
alpha = [0] * 26

for i in w:
    alpha[ord(i) - 65] += 1

if alpha.count(max(alpha)) > 1:
    print('?')
else:
    print(chr(alpha.index(max(alpha))+65))
