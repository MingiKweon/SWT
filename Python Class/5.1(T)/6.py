m,n,x = map(int,input().split())

if m*n < x:
    print("0 0")
else:
    r = (x-1) // n + 1 #시작을 0이라고 생각
    c = (x-1) % n + 1
    print(r,c)