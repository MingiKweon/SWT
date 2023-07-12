import time
n = int(input())

start_time = time.time()
for i in range(2 , n):
    if n % i == 0:
        print("해당 숫자는 소수가 아닙니다.")
        break
else:
    print("해당 숫자는 소수입니다.")

print("걸린시간:{}".format(time.time() - start_time))