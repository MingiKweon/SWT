print(" "+"*"*4)

n= int(input())

num= 1

for m in range(n):
    print(" "*(n-num) + "*"*num)
    num+= 1