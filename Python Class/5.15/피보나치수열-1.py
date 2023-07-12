#피보나치 수열이란
#전항과 전전항의 합을 해당 항의 값으로 설정하는 수열


#1 1 2 3 5 8 ....
# counter = 0
# def Fibo(n):
#     global counter
#     counter += 1
#     if n == 0 or n == 1: #n<2
#         return n
#     else:
#         return Fibo(n-1) + Fibo(n-2)
    
# print(Fibo(3))
# print(counter)

n = int(input()) # n = 5

for i in range(1,n+1):
    x = 0
    y = 1

    if n == 1:
        num = x
        break
    elif n == 2:
        num = y
        break
    else:
        x, y = y, x + y
        num = 
