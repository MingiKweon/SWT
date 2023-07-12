n = int(input())

for i in range(1,2*n):
    if i == 1:
        print(" "*(i-1) + "*"*(2*n-1-2*(i-1)) + " ")
    elif i <= n:
        print(" "*(i-1) + "*"*(2*n-1-2*(i-1)))
    else:
        print(" "*(2*n-i-1) + "*"*((2*n-1)-2*(2*n-i-1)))
    