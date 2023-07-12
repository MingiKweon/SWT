a = [1,2,34,5,6,7,897]

del a[6]
print(a)

if 1 in a:
    print("True")
else:
    print("False")

print()
print()
print()

a = []
for i in range(100):
    a.append(i)
print(a)
for j in range(100):
    del a[j]
print(a)