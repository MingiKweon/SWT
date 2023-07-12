a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a >= 40:
    ra = a
else: 
    ra = 40

if b >= 40:
    rb = b
else: 
    rb = 40

if c >= 40:
    rc = c
else: 
    rc = 40

if d >= 40:
    rd = d
else:
    rd = 40

if e >= 40:
    re = e
else: 
    re = 40

print(int((ra+rb+rc+rd+re)//5)) #이 과정을 10039.py에서는 sum으로 처리해서, 더해주는 식으로 --> 그러면 여러변수를 적용할 필요없다.