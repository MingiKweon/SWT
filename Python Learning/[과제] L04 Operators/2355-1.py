a, b= map(int, input().split())

if a<=b:
    print(int(((a+b)/2)*(b-a+1)))
else: 
    print(int(((a+b)/2)*(a-b+1)))


