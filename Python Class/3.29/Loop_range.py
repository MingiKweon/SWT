n = int(input())

for i in range(1,n+1):
    print(i)
    n += 1 # 이건 왜 안됨(내가 생각한건 n이 for문 안에서 작동해서 무한으로 실행되는걸 바랬는데)
