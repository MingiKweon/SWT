a , b = input().split()

c = []
c.append(a[::-1])
c.append(b[::-1])

print(max(c))

print("========")

print(a[::-1]) if int(a[::-1]) > int(b[::-1]) else print(b[::-1]) #삼항연산자
print()
print(a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1])