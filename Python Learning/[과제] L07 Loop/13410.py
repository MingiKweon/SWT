n , k = map(int , input().split())

num_list = []
for i in range(1 , k + 1):
    num_list.append(int(str(n * i)[::-1]))

print(max(num_list))