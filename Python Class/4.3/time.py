import time
print(time.time())

start_time = time.time()

for i in range(10000):
    print("*" , end=".")
print()
print("===============")

print(time.time() - start_time)