k = int(input())

arr = []
for i in range(k):
    n = int(input())
    arr.append(n)
    if k == 1:
        pass
    else:
        if n == 0:
            arr.pop()
            arr.pop()

print(sum(arr))
