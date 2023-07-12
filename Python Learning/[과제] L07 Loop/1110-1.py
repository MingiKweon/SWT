n = input()
m = int(n)

if int(n) < 10:
    n = "0" + n

nn = str(int(n[0])+int(n[1]))

if int(nn) >= 10:
    nn = nn[1]

nn2 = n[1] + nn

num = 1

while int(nn2) != m:
    nn = str(int(nn2[0]) + int(nn2[1]))
    if int(nn) >= 10:
        nn = nn[1]
    nn2 = nn2[1] + nn
    num += 1


print(num)