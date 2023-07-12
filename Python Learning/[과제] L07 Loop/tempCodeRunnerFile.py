n = input()
m = int(n)

if int(n) < 10:
    n = "0" + n

nn = n[0]+n[1]

if int(nn) >= 10:
    nn = nn[1]

nn2 = n[1] + nn

num = 1

while nn2 != m:
    nn = int(nn2[0]) + int(nn2[1])
    if int(nn) >= 10:
        nn = nn[1]
    nn2 = nn2[1] + nn
    num += 1


print(num)