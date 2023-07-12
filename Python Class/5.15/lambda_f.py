def my_adder(a,b):
	return a + b

my_adder = lambda a , b: a + b

print(my_adder(1,2))


arr = [1,2,4,5]
for i, x in enumerate(arr):
	print(i,x)

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
	
print(factorial(4))