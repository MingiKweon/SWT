a,b = map(int,input().split())

a,b = min(a,b) , max(a,b)

for i in range(a,b+1):
    print(i,end=" ")