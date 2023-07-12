n = int(input())

for i in range(n):
    if n == 1:
        print("*")
        break
    elif n % 2 == 1: 
        print("*"+" *"*(n//2))
        print(" *"*(n//2))
    else:
        print("*"+" *"*(n//2-1))
        print(" *"*(n//2))
            