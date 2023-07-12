counter = 0

memo = {}

def fibo(n):
    global counter
    counter += 1

    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = fibo(n-2) + fibo(n-1)
        return memo[n]

n = int(input())
print("{}번째 피보나치 수: {}".format(n, fibo(n)))
print("총 {}번 연산했습니다.".format(counter))