n = int(input())

for i in range(n):
    m = list(map(int,input().split()))
    mn = sum(m[1:]) / m[0]
    total = 0
    for j in range(1,m[0]+1):
        
        if m[j] > mn:    
            total += 1
    percentage = total / m[0] * 100
    formatted_str = "{:.3f}".format(percentage)
    print(f'{formatted_str}%')


