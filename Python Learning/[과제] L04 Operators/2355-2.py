a , b = map(int,input().split())
if max(a,b) == a:
    a = b
    b = a

total = 0
for i in range(a,b+1):
    total += i

print(total)