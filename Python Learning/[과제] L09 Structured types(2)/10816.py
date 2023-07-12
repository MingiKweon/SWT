card = {}

n = int(input())
numLst = list(map(int, input().split()))

for m in numLst:
    if m in card:
        card[m] += 1
    else:
        card[m] = 1
 

k = int(input())
numLst2 = list(map(int,input().split()))

for j in numLst2:
    if j in card:
        print(card[j], end=" ")
    else:
        print(0, end=" ")
