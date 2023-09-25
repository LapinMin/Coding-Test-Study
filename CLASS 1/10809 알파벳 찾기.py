alphabet = [chr(i) for i in range (97, 97+26)]

string = input()

for s in alphabet:
    if s in string:
        print(string.index(s), end=' ')
    else:
        print(-1, end=' ')