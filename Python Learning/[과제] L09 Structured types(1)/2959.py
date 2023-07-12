#r,l,b,f = map(int,input().split())
#
#if r>l:
#    print(0)
#else:
#    if f<b:
#        print(0)
#    else:
#        print(min(b,f) * min(r,l))
#해당 알고리즘은 r,l,b,f처럼 정해진 순서가 있을 경우이다.

numList = list(map(int,input().split()))

numList.sort()
print(numList[0]*numList[2]) #일명의 소거법/규칙 찾기의 과정이 필요할듯
