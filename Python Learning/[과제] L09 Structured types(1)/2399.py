n = int(input())

sum = 0
numList = list(map(int,input().split()))
for i in numList:
    for j in numList:
        sum += abs(i-j)
print(sum)

#시간초과