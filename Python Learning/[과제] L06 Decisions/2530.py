a, b, c= map(int, input().split())
d= int(input())

sec_d= a*3600+b*60+c+d

x= sec_d//3600
y= (sec_d%3600)//60
z= (sec_d%3600)%60

#if x>=24: #이거 안 적어도 됨!! 
x= x%24

print(x,y,z)


##