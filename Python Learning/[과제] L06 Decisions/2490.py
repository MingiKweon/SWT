a= list(map(int, input().split()))
b= list(map(int, input().split()))
c= list(map(int, input().split()))

num= [a, b, c]
for i in num:
    if i.count(0)==0:
        print("E")
    elif i.count(0)==1:
        print("A")
    elif i.count(0)==2:
        print("B")
    elif i.count(0)==3:
        print("C")
    else:
        print("D")




