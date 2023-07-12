n = int(input())

if n % 5 == 0:
    print(n // 5)
elif n % 5 == 1:    
    if n == 1:
        print(-1)
    else:
        print((n // 5) + 1)
elif n % 5 == 2:
    if ... #귀납적으로 규칙을 찾아줘도 괜찮