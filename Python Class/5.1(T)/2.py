#별
n = int(input())

if n == 1:
    print("*")
else:  
    print("*")
    for i in range(n-2):
        print("*" + (" "*i) + "*")
    print("*"*n)
