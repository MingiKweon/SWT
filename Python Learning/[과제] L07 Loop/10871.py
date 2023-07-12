a , b = map(int , input().split())
num_list = list(map(int , input().split()))
num = []

for i in num_list:
    if i < b:
        num.append(i)

for j in num:
    print(j , end=" ")