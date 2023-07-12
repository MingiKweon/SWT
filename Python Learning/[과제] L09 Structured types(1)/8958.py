n = int(input())

for i in range(n):
    num_lst = list(input())
    total = 0
    total_score = 0

    for j in num_lst:
        if j == 'O':
            total += 1
            total_score += total
        else: 
            total = 0
    print(total_score)
        