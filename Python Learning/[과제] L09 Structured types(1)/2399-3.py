n = int(input())
nums = list(map(int, input().split()))

s = 0
for x in nums:
    for y in nums:
        s += abs(x-y)

print(s)