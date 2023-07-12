n = int(input())

for i in range(1,2*n):
    if i <= n:
        print(" "*(i-1)+"*"*(2*n+1-2*i))
    else:
        print(" "*(2*n-(i+1))+"*"*(2*n-1 -2*(2*n-(i+1))))