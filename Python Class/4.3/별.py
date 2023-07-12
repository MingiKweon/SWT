n= int(input())

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print("===========")


for m in range(n):
    print("*"*n, end="")
    print()