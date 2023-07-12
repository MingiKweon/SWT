a, b= map(int, input().split())

sum= 0
for i in range(a,b+1,1):
    sum+=i
print(sum)


print("------")

print(int(((a+b)/2)*(b-a+1)))

print("------")

num= b-a+1
sum= num*(a+b)/2
print(int(sum))