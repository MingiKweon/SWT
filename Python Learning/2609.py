a , b = map(int, input().split())
m = a
n = b
if a > b:
    while a % b != 0:
        temp = a
        a = b
        b = temp % b
    else:
        print(b)
        print(m*n//b)
else:
    while b % a != 0:
        temp = b
        b = a
        a = temp % a
    else:
        print(a)
        print(m*n//a)