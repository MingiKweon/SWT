import math
n = input()

sum = 0
for i in n:
    if i.islower() == True:
        sum += ord(i) - 96
    else: 
        sum += ord(i) - 38

prime = True


for j in range(2,int(math.sqrt(sum))+1):
    if sum % j == 0:
        prime = False
if prime == True:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
