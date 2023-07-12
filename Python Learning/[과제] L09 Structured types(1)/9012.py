n = int(input())


for i in range(n):
    arr = []
    m = input()
    for j in m:
        if j == "(":
            arr.append("(")  
        else:
            if len(arr) != 0:
                arr.pop()
            else:
                print("NO")
                break
    else:
        if len(arr) == 0:
            print("YES")
        else:
            print("NO")