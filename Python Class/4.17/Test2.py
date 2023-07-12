num = [1,2,3,45,6]
print(num)

num[2] = 13
print(num)

num.append(0)
print(num)

num.insert(len(num),34)
print(num)

if len(num) == 0:
    num.clear()
    print(num)
else:
    num.pop(2)
    print(num)
    