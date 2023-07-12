a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

score = [a, b, c, d, e]
total = 0

for i in score:
    if i >= 40: #반복문이라 다른 변수를 사용할 수가 없음...
        total += i
    else: 
        total += 40

    

print(total//5)