n = int(input())
arr = list(range(2,n+1))

for i in range(2,n+1):
    for j in range(i+1,n+1):
        if j in arr and j % i == 0:
            arr.remove(j)
        
print(arr)
            