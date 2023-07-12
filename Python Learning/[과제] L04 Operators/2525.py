a= map(int, input().split()) #list라서 더하기가 쉽지 않음
a=list(a)
b= int(input())

c= b//60
d= b%60

x= a[0]
y= a[1]

x+= c
y+= d


if x>= 24:
    x= x-24 #x-=24
if y>= 60:
    x= x+1
    y= y-60
if x==24:
    x= 0

print(f"{x} {y}")