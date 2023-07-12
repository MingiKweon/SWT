n = int(input())

prime = []
for _ in range(n):
    prime.append(True)
    
for i in range(2,n+1):
    if prime[i] == True:
        for j in 