a= int(input())
b= int(input())

x= b//100
z= b%10
y= (b%100-z)//10

print(a*z)
print(a*y)
print(a*x)
print(a*b)


print("-----------")

b= str(b)

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))