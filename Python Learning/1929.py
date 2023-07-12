import math
n , m = map(int,input().split())

for i in range(n,m+1):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            break
    else: 
        if i != 1:
            print(i)
    
        