a , b = map(int,input().split())
c = int(input())


ft = a * 60 + b + c
ftt = ft // 60
ftm = ft % 60
if ftt == 24:
    ftt = 0

print(ftt,ftm)
    