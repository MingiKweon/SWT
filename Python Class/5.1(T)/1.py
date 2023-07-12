#에라토스테네스의 체

n = int(input())

primes = [True]* (n+1)

primes[0] = False
primes[1] = False

s = 0
for i in range(2,n+1):
    if primes[i]:
        s += i
        for j in range(i*2,n+1,i):
            primes[j] = False

print(s)
