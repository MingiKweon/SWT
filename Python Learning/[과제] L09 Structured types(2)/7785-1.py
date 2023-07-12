n = int(input())

arr = {}
for i in range(n):
    x , y = input().split()

    if y == "enter":
        arr.update({x:y})
    else:
        del arr[x]

arr = sorted(arr.keys(), reverse=True)
for j in arr:
    print(j)

