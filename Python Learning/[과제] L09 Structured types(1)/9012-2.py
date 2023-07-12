#stack의 동작원리 // 자료구조


n = int(input())
for i in range(n):
    ps = input()
    
    s = 0
    for x in ps:
        if x == '(':
            s += 1
        elif x == ')':
            s -= 1
            if s < 0:
                print("NO")
                break
    else:
        if s != 0:
            print("NO")
        else:
            print("YES")