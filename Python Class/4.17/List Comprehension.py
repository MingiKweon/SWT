#range(1,11) == [1,2,3,4,5,6,7,8,9,10]

print([num**2 for num in range(1,11) if num == 2 or 5])

a = ['a','v','d']
b = sorted(a,reverse=True)

print(id(a))
print(b)
print(id(b))