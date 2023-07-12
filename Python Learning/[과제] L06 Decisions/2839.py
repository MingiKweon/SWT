n= int(input())
num=0

while n>=0:
    if n%5==0:  #n%5==3
        num += int(n//5)
        print(num)
        break
    n-=3
    num += 1
else:
     print(-1)


