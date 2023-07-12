n = input()

if int(n) < 10:
    n = "0" + n

cyc = 1
m1 = int(n[0]) + int(n[1])
if m1 >= 10:
    m1 = m1 -10
m2 = n[1] + str(m1)

while n != m2:
    m1 = int(m2[0]) + int(m2[1])
    if m1 >= 10:
        m1 = m1 -10
    m2 = m2[1] + str(m1)
    
    cyc += 1

print(cyc)