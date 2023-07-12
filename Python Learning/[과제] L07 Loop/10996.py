n = int(input())

for i in range(n):
    if n == 1:
        print("*")
    else:
        print("* "*(n - n//2))
        print(" *"*(n//2))