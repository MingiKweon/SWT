#n개의최대공약수

n = int(input())
nums = list(map(int,input().split()))

print(nums)
gcd = nums[0]

for i in nums[1:]:
    a = max(gcd,i)
    b = min(gcd,i)

    while b !=0:
        a, b = b , a % b

        gcd = a
print(gcd)