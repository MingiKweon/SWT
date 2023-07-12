n = int(input())

numList = list(map(int,input().split()))
numList.sort()

sum = 0
for i in range(n):
    sum += numList[i]*(4*i-2*n+2) #/ 2*i x nums[i] - 2*(n-i-1) x nums[i] 규칙찾기

print(sum)