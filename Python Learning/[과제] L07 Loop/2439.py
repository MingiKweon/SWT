n= int(input())

num= 1


for i in range(n):
    blank= " "*(n-num)
    star= "*"*num
    print(f"{blank}{star}")
    
    num+= 1

print("=========")

num= 1

for m in range(n):
    print(" "*(n-num) + "*"*num)
    num+= 1

