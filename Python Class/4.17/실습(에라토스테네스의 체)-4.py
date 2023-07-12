n = 51
prime = [True for _ in range(52)]
primeList = []
for i in range(2,52):
    if prime[i] == True:
        for j in range(i*2,52,i):
            prime[j] = False
        primeList.append(i)
    
print(primeList)
    

    