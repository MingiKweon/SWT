n = int(input())
m = int(input())

total = 0

for i in range(m):
    a, b = map(int , input().split())
    total += (a*b)

if total == n:
    print("Yes")
else:
    print("No")