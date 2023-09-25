n = int(input())

for _ in range(n):
    h, w, m = map(int, input().split())
    
    a = (m-1)%h+1
    b = (m-1)//h+1
    print(a*100+b)