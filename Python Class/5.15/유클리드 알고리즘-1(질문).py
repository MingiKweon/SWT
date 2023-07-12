#유클리드 알고리즘: 최대공약수 찾는거
#재귀 함수로 만들어보기

#14 34, 2
#34 / 14 = 2.. 6

#14 6
#14 / 6 = 2.. 2

#6 / 2 = 3.. 0


def f(a,b):
    a = max(a,b)
    b = min(a,b)
    

    if a % b == 0:
        return b
        
    else:
        return f(b, a % b)
    
# print(f(14,34))


print(list(map(f, [4],[5])))





# def gcd( a , b ) :
#     if b == 0 :
#         return a
#     else :
#         return gcd(b, a % b)

# print(gcd(14,34))

