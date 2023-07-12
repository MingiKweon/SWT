import math
n = int(input("숫자를 입력하세요: "))

for i in range(2,int(math.sqrt(n)+1)):
    if n % i == 0:
        print("소수가 아닙니다.")
        break
    else:
        print('소수입니다.')

